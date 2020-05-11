openssl rand -hex 6| sed -e 's/\(..\)/\1:/g' -e 's/.$//'
