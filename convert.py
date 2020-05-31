import codecs

src = "dump_data.json"
dst = "dump_data_new.json"
source = codecs.open(src, "rb").read().decode('unicode-escape')
codecs.open(dst, "wb","utf-8").write(source)