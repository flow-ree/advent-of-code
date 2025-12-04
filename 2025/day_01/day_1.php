<?php
// file
$file = file("input.txt");

$dial = 50;
$points = 0;

foreach($file as $line)
{
    $direction = substr($line, 0, 1);
    $clicks = (int) substr($line, 1, strlen($line));
    if ($clicks === 992) {
        echo $line;
        echo $dial . PHP_EOL;
    }
    switch ($direction)
    {

        case 'L':
            $end = $dial - $clicks;

            $abs =  abs($end) % 100 === 0 ? 0 : 100 - (abs($end) % 100);

            $dial = $end < 0
                ? $abs
                : $end;
            break;

        case 'R':
            $end = $dial + $clicks;
            $abs = (abs($end % 100));


            $dial = $end > 99
                ? $abs
                : $end;
            break;
    }
    if ($clicks === 992) {
        echo $dial . PHP_EOL;
    }

    if ($dial == 0)
    {
        // echo $line;
        $points++;
    }
}

echo "password is: " .  $points . PHP_EOL;