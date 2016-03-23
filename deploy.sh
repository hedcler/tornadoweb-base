rsync -e ssh -rt \
--modify-window=2 \
--exclude '.git*' \
--exclude 'venv' \
--exclude '__pycache__' \
--exclude '*.pyc' \
--exclude '*.conf' \
--exclude 'requirements_dev.txt' \
--stats -v ./* $2@$1:$3