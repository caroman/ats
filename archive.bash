version="$1"

git archive master | bzip2 > irgt-site-"$1".tar.bz2

