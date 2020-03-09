# Compare DICOM files tag by tag.

Usage:

```
python diffcom.py file1 file2
```

file1 is often the earlier, whereas file2 is the later.

e.g.,

```
$ pip install -r requirements.txt
$ python diffcom.py samples/rtplan0.dcm samples/rtplan1.dcm
[A] (0008,0005) Specific Character Set                   CS "ISO 2022 IR 6"
[=] (0008,0012) Instance Creation Date                   DA "20030903"
[=] (0008,0013) Instance Creation Time                   TM "150031"
[=] (0008,0016) SOP Class UID                            UI "1.2.840.10008.5.1.4.1.1.481.5"
[=] (0008,0018) SOP Instance UID                         UI "1.2.777.777.77.7.7777.7777.20030903150023"
[M] (0008,0020) Study Date                               DA [1] "20030716" [2] "20200310"
[=] (0008,0030) Study Time                               TM "153557"
[=] (0008,0050) Accession Number                         SH ""
[=] (0008,0060) Modality                                 CS "RTPLAN"
[=] (0008,0070) Manufacturer                             LO "Manufacturer name here"
[=] (0008,0080) Institution Name                         LO "Here"
[=] (0008,0090) Referring Physician's Name               PN ""
[=] (0008,1010) Station Name                             SH "COMPUTER002"
[=] (0008,1040) Institutional Department Name            LO "Radiation Therap"
[=] (0008,1070) Operators' Name                          PN "operator"
[=] (0008,1090) Manufacturer's Model Name                LO "Treatment Planning System name here"
[M] (0010,0010) Patient's Name                           PN [1] "Last^First^mid^pre" [2] "Arai^Tatsuhiko"
[=] (0010,0020) Patient ID                               LO "id00001"
[=] (0010,0030) Patient's Birth Date                     DA ""
[=] (0010,0040) Patient's Sex                            CS "O"
[D] (0018,1020) Software Versions                        LO "softwareV1"
...snip...
```

|Mark |Means     |
|:---:|:---------|
| [=] | Same tag |
| [A] | Added to file2 |
| [M] | Modified to file2 |
| [D] | Deleted to file2 |
