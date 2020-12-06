<?php
$lines = array();
$in = fopen("./01.txt", 'r') or die("failed opening file.");
while(!feof($in)) {
	array_push($lines, intval(fgets($in)));
}
fclose($in);

function parse($stuff) {
	foreach ($stuff as $value) {
		$diff = 2020 - $value;
		if (in_array($diff, $stuff))
			return $diff * $value;
	}
}

printf("%d\n", parse($lines));
?>
