DIR=$(dirname $(dirname $(readlink -f $0)))
FASTA=$DIR/data/test.fa
FASTQ=${FASTA:0:-1}q
sed -n 'n;p' $FASTA > $DIR/tests/fasta-check.txt
sed -n '2~4p' $FASTQ > $DIR/tests/fastq-seq.txt
sed -n '4~4p' $FASTQ > $DIR/tests/fastq-quality.txt

paste -d '|' $DIR/tests/fastq-seq.txt $DIR/tests/fastq-quality.txt > $DIR/tests/fastq-check.txt 
