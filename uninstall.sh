#/bin/sh
if [ "$(id -u)" != "0" ]; then
	echo "You need to run this script with superuser privileges."
	echo "Aborting.."
	exit 1
fi

echo "Uninstalling.......please wait...."
rm -rf /opt/g0dray.py
rm /usr/local/bin/g0dray.py
echo "Done."

