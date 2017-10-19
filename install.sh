#/bin/sh
if [ "$(id -u)" != "0" ]; then
	echo "You need to run this script You need to run this script with superuser privileges."
	echo "Aborting.."
	exit 1
fi

echo "Installing.......please wait...."
mkdir /opt/g0dray.py
cp -r * /opt/g0dray.py/
chmod +x /opt/g0dray.py/src/g0dray.py
ln -sr /opt/g0dray.py/src/g0dray.py /usr/local/bin/g0dray.py
echo "Install finished with no errors."

