# Blocks and Slots
When Analysis manipulates a single FID, that FID is contained inside a dataset. Each dataset contains blocks that represent processing steps. This document describes how Analysis stores those blocks internally while running. It assumes a basic working knowledge of Python, or at least some object-oriented programming experience.

## The Slots
At present, there are four _slots_ in the blocks container. Their names are raw, prep, spectral and fit. At some point, a fifth slot for spatial processing will probably be added between prep and spectral. (Note: don't confuse the term "slots" with Python's special `__slots__` attribute. The slots described here have nothing to do with the Python attribute.)

The blocks are stored in an ordered dictionary that is keyed by the slot names ("raw", "prep", etc.).

Slots are never empty. If a slot doesn't need to do anything (this is often the case with prep), it's populated with an identity version of the block that simply returns whatever data is handed to it.

The raw slot is somewhat of an exception to the rule above. It's always populated, but it never contains an identity instance because there is no BlockRawIdentity class. (See below.)

## Identity Blocks
The simplest version of each block is the _identity_ block. Blocks are transformative (except for raw, which is just an inert container) and identity blocks are named for the identity transform in mathematics. Since the raw block is never transformative, there is no BlockRawIdentity.

By default, a new dataset starts with a BlockRaw object in the first slot and identity blocks in all other slots (BlockPrepIdentity, BlockSpectralIdentity, etc.). In practice, BlockSpectralIdentity is always replaced with BlockSpectral. (This mirrors what happens in Analysis' GUI -- there is always a spectral tab.) The practical upshot is that it's perfectly fine (even common) to have a mix of identity and non-identity blocks in a dataset.

## Non-identity Blocks
All blocks in a given slot must subclass (derive from) the identity class for that slot. For instance, BlockPrepFidsum inherits from BlockPrepIdentity. The identity class (in combination with the base Block class) describes the minimum implementation for a block of that type.

Deriving from a particular identity class allows other code in Analysis to know in which slot a block instance resides by using `isinstance()`. Remember that `isinstance(A, B)` returns True if A is of class B or a subclass thereof. For example, this statement returns True -- 

```
#!python isinstance(block_prep_fidsum.BlockPrepFidsum(), block_prep_identity.BlockPrepIdentity)
```

## Attachments
Attached are two files. AnalysisSlotsAndBlocks.odg is the LibreOffice Draw source file for [raw-attachment:AnalysisSlotsAndBlocks.png]. The latter shows Analysis' slots and blocks in three states. 

The first state is the not-very-useful default where all of the transformative blocks are identities. 

The second state shows the minimum useful set of blocks -- BlockSpectralIdentity has been replaced by BlockSpectral. This is the state of the blocks when Analysis imports 3rd party data.

The third state shows an example of the prep and fit blocks being replaced.

In all of these examples, the spatial slot and blocks are "ghosted" because at this point a working version is just a figment of our imaginations.
