echo "Total Param= $#,  PROG: $0, param1 = $1, param2 = $2";

if [ "$#" -lt 1 ]; then
    echo "$# 쇼핑몰 고유 이름을 입력 해주세요."
    echo "Usage: $0 [options]"
	exit 1
fi

CRAWL_DIR="/home/spchoi/codes/sp_scripts/fitzme-crawling_for_test"
BRAND=$1
COMPOSE_YAML=$CRAWL_DIR/compose/prod.yml

if [ -d $CRAWL_DIR/$BRAND ]; then
    # image build
    docker-compose \
        --project-directory $CRAWL_DIR \
        -f $COMPOSE_YAML \
        up -d --build 

    docker-compose \
        --project-directory $CRAWL_DIR \
        -f $COMPOSE_YAML  \
        run  -w /app/$BRAND fitzme-crawling python crawler_cls.py
else
    echo "File" $CRAWL_DIR/$BRAND  "does not exist"
fi


