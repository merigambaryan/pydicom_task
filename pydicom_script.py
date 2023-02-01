import os
import pydicom as dicom

def anonymize_and_move(dcm_file):
    # получение содержимого файла .dcm
    ds = dicom.dcmread(dirName + '/' + dcm_file)

    # создание каталога StudyInstanceUID
    if not os.path.isdir(os.path.join(outDirName, ds.StudyInstanceUID)):
        os.mkdir(os.path.join(outDirName, ds.StudyInstanceUID))

    # создание каталога SeriesInstanceUID
    if not os.path.isdir(os.path.join(outDirName + '\\\\' + ds.StudyInstanceUID, ds.SeriesInstanceUID)):
        os.mkdir(os.path.join(outDirName + '\\\\' + ds.StudyInstanceUID, ds.SeriesInstanceUID))

    patient_name = 'Anonymous'
    # анонимизация файла
    ds.PatientName = patient_name

    # изменение название файла на SOPInstanceUID.dcm и
    # перемещение файла в новую директорию
    ds.save_as(outDirName + '\\\\' + ds.StudyInstanceUID + '\\\\' + ds.SeriesInstanceUID \
                 + '\\\\' + ds.SOPInstanceUID + '.dcm')

    # запись в файл сопоставления путей
    with open('pathmatching.txt', 'a', encoding='utf-8') as pathmatching_file:
        print(dirName + '\\' + dcm_file + ' - > ' + outDirName + '\\' + ds.StudyInstanceUID + \
              '\\' + ds.SeriesInstanceUID + '\\' + ds.SOPInstanceUID + '.dcm\n', \
              file=pathmatching_file)


# имя директории с файлами .dcm
dirName = 'src'
# имя новой директории
outDirName = 'src_out'


# извлечение всех файлов из директории исходной директории
list_files_dcm = os.listdir(dirName)

# создание файла сопоставления путей
f = open('pathmatching.txt', 'w', encoding='utf-8')
f.close()

# работа с файлами и преобразование структуры хранения файлов .dcm
for dcm_file in list_files_dcm:
    # проверка расширения файла
    if os.path.splitext(dcm_file)[1] == '.dcm':
        anonymize_and_move(dcm_file)
