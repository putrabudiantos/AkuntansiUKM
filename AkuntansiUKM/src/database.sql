DROP TABLE IF EXISTS detailperusahaan;
DROP TABLE IF EXISTS laporanjurnal;


CREATE TABLE laporanjurnal(
    tanggal DATE,
    keterangan VARCHAR(100),
    debet INT(255),
    kredit INT(255) 
)ENGINE=InnoDB;


CREATE TABLE detailperusahaan(
    nama VARCHAR(100),
    alamat VARCHAR(100),
    telp INT(100),
    email INT(100) 
)ENGINE=InnoDB;


