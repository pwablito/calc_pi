#!/usr/bin/perl
$n = '1000000';
$n = $n + 0;
$h = $n * 0;
for($a = 1; $a < $n; $a = ++$a){
    $t = $a/$n;
    $val = (1-(($t)**2))**0.5;
    $h+=$val;
}
$h = $h*2;
$pi = (2/$n)*(1+$h);
printf "%.11f", $pi;
