import filehydra_pkg.filehydra.filehydra_core as fh



fq=fh.FileQueue("C:\\Users\\EUROCOM\\Documents\\Git\\DovaX\\forloop-projects\\idealista","high_level_queue")
template=fh.FileTemplate("", "txt")
filename,data=fq.process_next_file(template)

print(filename,data)