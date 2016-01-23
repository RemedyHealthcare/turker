import sys, os, argparse
import cPickle as pickle
import csv

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Create Turk Input', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--dataDir', type=str, default="data", help='Where the data is stored')
    parser.add_argument('--outputFile', type=str, default="input.csv", help='Where the results will be written')
    flags = parser.parse_args()

    input_files = []

    for (dir, _, files) in os.walk(flags.dataDir):
        for f in files:
            path = os.path.join(dir, f)
            if ".p" in path:
                input_files.append(path)

        print path

    with open(flags.outputFile, 'wb') as csvfile:

        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['title', 'link', 'selection', 'target'])

        for f in input_files:

            wiki = pickle.load(open(f, "rb"))

            wiki['sentences'] = [x.encode('utf-8') for x in wiki['sentences']]

            for i in xrange(len(wiki['sentences'])):
                target = wiki['sentences'][i]
                start = max(0, i - 3) 
                end =  min(len(wiki['sentences']), i + 3)
                writer.writerow([wiki['title'], wiki['url'], " ".join(wiki['sentences'][start:end]), wiki['sentences'][i]])



