
import os
import xlrd
from downloader import Downloader
from processor import CreateDataFile
from customsuperimposer import CustomSuperImposer
import xlsxwriter

def main():
    # Downloader().download('proteins.csv')
    # for file in os.listdir('pdbs'):
    #     structure = file.split('.')[0]
    #     print(structure)
    #     CreateDataFile().create(structure, 'pdbs/'+file)

    files = os.listdir('outputs')
    for i in range(0, 39):
        #i=0
        data = []
        for file in files:
            print(file)
            book = xlrd.open_workbook('outputs/'+file)
            sh = book.sheet_by_index(i)
            for rx in range(sh.nrows):
                values = sh.row_values(rx)
                d = {}
                if rx == 0:
                    pass
                else:
                    d['seq'] = values[0]
                    d['start'] = int(values[1])
                    d['end'] = int(values[2])
                    d['resolution'] = values[3]
                    d['structure_id'] = values[4]
                    d['chain'] = file.split('-')[1].split('.')[0]
                if d:
                    data.append(d)

            result = CustomSuperImposer().superimposetest(data)
            if result:
                excelwrite(i+3, result)

def excelwrite(seqcount, result):
    output_file = 'finaloutputs/'+str(seqcount)+'.xlsx'
    workbook = xlsxwriter.Workbook(output_file)
    worksheet = workbook.add_worksheet(name='result')
    worksheet.write(0, 0, "seq")
    worksheet.write(0, 1, "Start")
    worksheet.write(0, 2, "End")
    worksheet.write(0, 3, "Resolution")
    worksheet.write(0, 4, "Chain")
    worksheet.write(0, 5, "ID")
    worksheet.write(0, 6, "seq")
    worksheet.write(0, 7, "Start")
    worksheet.write(0, 8, "End")
    worksheet.write(0, 9, "Resolution")
    worksheet.write(0, 10, "Chain")
    worksheet.write(0, 11, "ID")
    worksheet.write(0, 12, "RMS Value")
    worksheet.write(0, 13, "Duplicate Count")
    worksheet.write(0, 14, "Type")
    row = 1
    col = 0
    #Iterate over the data and write it out row by row.
    finalvalues = {}
    for r in result:
        first = r[0]
        rms = r[2]

        if first['seq'] not in finalvalues:
            print("not in:{}".format(first['seq']))
            finalvalues[first['seq']] = r
            finalvalues[first['seq']].append(1)
        else:
            existing = finalvalues[first['seq']]
            print("Already existing:{} and count:{}".format(first['seq'],
                                                            existing[3]))
            if existing[2] > r[2]:
                finalvalues[first['seq']] = r
                finalvalues[first['seq']].append(existing[3])
            finalvalues[first['seq']][-1] += 1
    #print("Finalvalues:{}".format(finalvalues))
    for res in finalvalues:
        r = finalvalues[res]
        first = r[0]
        second = r[1]
        rms = r[2]
        worksheet.write(row, col, first['seq'])
        worksheet.write(row, col+1, first['start'])
        worksheet.write(row, col+2, first['end'])
        worksheet.write(row, col+3, first['resolution'])
        worksheet.write(row, col+4, first['chain'])
        worksheet.write(row, col+5, first['structure_id'])
        worksheet.write(row, col+6, second['seq'])
        worksheet.write(row, col+7, second['start'])
        worksheet.write(row, col+8, second['end'])
        worksheet.write(row, col+9, second['resolution'])
        worksheet.write(row, col+10, second['chain'])
        worksheet.write(row, col+11, second['structure_id'])
        worksheet.write(row, col+12, rms)
        worksheet.write(row, col+13, r[3])
        worksheet.write(row, col+14, find_type(first['seq'], seqcount))
        row+=1

    workbook.close()

def find_type(seq, splitnum):
    vals = []
    indexes = []
    for x in range(0,len(seq)+1, 3):
            indexes.append(x)
    count = 0
    while count<len(indexes):
        if count == len(indexes) - 2:
            vals.append(seq[indexes[count]:indexes[count+1]])
            break
        vals.append(seq[indexes[count]:indexes[count+1]])
        count+=1
    countval = {}
    for k in vals:
        if k not in countval:
            countval[k] = str(vals.count(k))
    return ''.join(countval.values())




if __name__ == '__main__':
    main()
    #find_type('ASNGLNTHR', 3)