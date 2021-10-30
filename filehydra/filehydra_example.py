import filehydra.filehydra_core as fh
fh=FileHydra()
result=fh.get_files_in_directory(fh.location, ".txt")
print(result)