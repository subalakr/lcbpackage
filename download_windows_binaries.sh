#!/bin/sh
ARCHES="x86 amd64"
VCVERS="9 10 11"
URIBASE="http://sdkbuilds.couchbase.com/job/lcb-win32-cmake"
LCBVERS=$1

for arch in $ARCHES; do
    for vers in $VCVERS; do
        for hostarch in 64 32; do
            url="$URIBASE/ARCH=$arch,MSVCC_VER=$vers,label=sdk_win2008_${hostarch}/ws/BUILD"
            url="${url}/libcouchbase-${LCBVERS}_${arch}_vc${vers}.zip"
            echo $url
            wget "$url"
        done
    done
done
