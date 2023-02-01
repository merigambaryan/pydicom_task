# pydicomtask

Задание:
Выполнить преобразования входных данных, используя модуль pydicom. 

 - удалить информацию хранящуюся в ключе PatientName (анонимизировать файлы)

 - используя информацию в ключах StudyInstanceUID, SeriesInstanceUID, SOPInstanceUID преобразовать структуру хранения файлов к следующей:

.на первом уровне StudyInstanceUID
.на втором уровне SeriesInstanceUID
(именем файла будет значение SOPInstanceUID с расширением .dcm)

Таким образом, путь к каждому файлу будет выглядеть так: $StudyInstanceUID/$SeriesInstanceUID/$SOPInstanceUID.dcm

дополнительно, нужно создать файл, в котором путь к каждому файлу исходной структуры сопоставлен пути к файлу в конечной структуре.# pydicom_task
