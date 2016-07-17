import scraper
import os


def collect_files(walk_dir, number_of_files=None):
    list_of_txts = []
    if number_of_files != None:
        counter = number_of_files
    else:
        counter = False
    print "Entering PDF Domain\n==================="
    for root, subdirs, files in os.walk(walk_dir):
        for filename in files:
            if filename.lower().endswith('.pdf'):
                print counter, filename
                file_path = os.path.join(root, filename)
                txtFromPdf = scraper.convert(file_path)
                list_of_txts.append(txtFromPdf)
                counter -= 1
                if counter and counter < 0:
                    return list_of_txts
    return list_of_txts
'''


            print('\t- file %s (full path: %s)' % (filename, file_path))

            with open(file_path, 'rb') as f:
                f_content = f.read()
                list_file.write(('The file %s contains:\n' % filename).encode('utf-8'))
                list_file.write(f_content)
                list_file.write(b'\n')
'''