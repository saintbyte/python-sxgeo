#!/bin/bash
set +ue
set -x
clearup()
{
  rm -f sxgeo.zip
}
mailme()
{
  echo "message: $1" | mail -s "sxgeo" admin@ural.im
}

wget -O"sxgeo.zip" https://sypexgeo.net/files/SxGeoCity_utf8.zip
CUR_MD5=`md5sum sxgeo.zip | cut -f1 -d" "`
LAST_MD5=""
LAST_MD5=`cat last_md5`
if [ ${CUR_MD5} == $LAST_MD5 ]
then
    MSG="Not need update"
    echo "$MSG"
    mailme "$MSG"
    clearup 
    exit 1
fi
echo -n $CUR_MD5 > last_md5
unar sxgeo.zip
clearup
if [ !-f "SxGeoCity.dat"]
then
    MSG="Dawn not found SxGeoCity.dat"
    echo "$MSG"
    mailme "$MSG"
    exit 2
fi
MSG="Seems OK"
echo "$MSG"
mailme "$MSG"
exit 0