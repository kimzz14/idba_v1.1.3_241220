############################################################################################
readDir=/archive/kimzz14/SRA_RAW/NAAS/Triticum_aestivum/Keumkang/NGS/data
prefix=$1
############################################################################################

python ./script/fq2fa.py \
    -1 ${readDir}/${prefix}_1.fastq.gz \
    -2 ${readDir}/${prefix}_2.fastq.gz \
    -o ${prefix}.fa

#readDir=/archive/kimzz14/SRA_RAW/NAAS/Triticum_aestivum/Keumkang/NGS/01.fastqSampler/result