# Export and Import Technical Notes
This is a brief review of some ideas related to import and export. For 
detailed documentation on the content of a Vespa import/export file, see
[the documentation for VIFF (Vespa Interchange File Format)](/wiki:VIFF/).


## Export and Import Concepts
 * Import is never destructive. It never overwrites anything in your existing 
   database. If it changes your database at all, it does so by adding to 
   what's already there.
   
 * Conflicts can arise between the names of existing objects and imported 
   objects. When a conflict arises, import creates a unique name for the 
   imported object. The current algorithm adds a timestamp to the name, and
   if that's still not unique it adds digits until a unique name is found.
   
 * You can import individual metabolites and pulse sequences from an
   experiment export file.


## Paths Not Taken
 * *Selective imports.* When the import code reads a file, it assumes 
   that every object it finds in the XML file that's not already in the 
   database should be added. The logic is simple.
   
 It might be nicer for the user if the import code examined the import 
 file and showed the user a list of importable objects (along with, perhaps,
 a list of objects in the import file that already exist in the database). 
 Naturally, the import dialog would give the user the opportunity to 
 select which items he wants to import.
   
 There's nothing wrong or even complicated about this approach, it's just
 another dialog and more to design, write, debug, document and maintain.
 
 * *Cancelling imports.* Another thing that a more sophisticated import
 GUI could do is offer the opportunity to cancel an in-progress import.

 * *Combining exports.* At present, export creates new or overwrites its
 target file. It doesn't offer the option to append to an existing file. 
 Furhtermore, export only exports one kind of object at a time (ignoring
 for the moment the fact that exporting experiments implies an export of 
 metabs and pulse sequences too). 
  
 There's no way, for instance, to export
 metabs and pulse sequences to the same file. Nor is there a way to 
 export one's entire database to a single file (unless one would be 
 satisified with only exporting in-use metabs and pulse sequences in which
 case exporting all experiments would be sufficient).
  
 There's no strong reason for this limitation, I just never wrote the code
 or designed the GUI to support combining export files.
