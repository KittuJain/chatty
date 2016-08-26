class File:
  def append(self, file_path, content):
    output_file = open(file_path, "a+")
    output_file.write(content)
    output_file.close()

  def read(self, file_path):
    return open(file_path, 'r')

