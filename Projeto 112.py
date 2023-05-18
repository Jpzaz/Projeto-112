import os 
import shutil 
# .exe , .msi, .gif, .png .jpg, .jpeg, .csv, .pdf , .xls , .xlsx , .ppt , .pptx from_dir = "C:/Users/ADMIN/Downloads" to_dir = "C:/WhiteHatJr/dowanloadedimages" list_of_files = os.listdir(from_dir) #print(list_of_files) # Mova todos os arquivos de imagem da pasta Downloads para outra pasta para file_name no list_of_files: nome, extensão = os.path.splitext(file_name) #print(nome) #print(extensão) se extensão == '': continue se extensão em ['.gif', '.png', '.jpg', '.jpeg','.jfif']: path1 = from_dir + '/' + file_name # Exemplo path1 : Downloads/ImageName1.jpg path2 = to_dir + '/' + "Image_Files" # Exemplo path2 : D:/My Files/Image_Files path3 = to_dir + '/' + "Image_Files" + '/' + file_name # Exemplo path3 : D:/My Files/Image_Files/ImageName1.jpg #print("path1 " , path1) #print("path3 ", path3) # Verifique se o caminho da pasta/diretório existe antes de mover




