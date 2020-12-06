<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);

function getInput(): array
{
    $rows = [];
    $f = fopen("input.csv", 'r');    
    while (!feof($f)) {
        $rows[] = fgetcsv($f, 4096)[0];                
    }
    return $rows;
}

function part1(): int
{
    $input = getInput();
    $total = count($input) - 1;
    $currentGroup = "";    
    
    return array_sum(
        array_map(function($row, $k) use(&$currentGroup, $total){                 
            $currentGroup .= $row;
            if(true === empty($row) || $k === $total){
                $sum = count(count_chars($currentGroup, 1));    
                $currentGroup = "";            
            }        
            return $sum ?? 0;
        }, $input, array_keys($input))
    ); 
}

function part2(): int
{
    $input = getInput();
    $total = count($input) - 1;
    $currentGroup = [];        
    
    return array_sum(
        array_map(function($row, $k) use(&$currentGroup, $total){                 
            
            if(false === empty($row)){
                $currentGroup[] = $row;
            }       
            
            if(true === empty($row) || $k === $total){                                               
                $expectedCount = count($currentGroup);                
                $sum = count(
                    array_filter(
                        count_chars(implode('', $currentGroup), 1),
                        function($charCount) use ($expectedCount){
                            return $charCount === $expectedCount;
                        })
                    );                                    
                    $currentGroup = [];            
                }            
                
                return $sum ?? 0;
            }, $input, array_keys($input))
        ); 
    }
    
    echo sprintf("result of part 1 is %d\n", part1());
    echo sprintf("result of part 2 is %d\n", part2());