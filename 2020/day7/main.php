<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);

const MY_BAG = "shiny gold";

function getInput($sep = ";"): array
{
    $rows = [];
    $f = fopen("input.csv", 'r');
    while (!feof($f)) {
        $row = fgetcsv($f, 4096, $sep);
        if(is_array($row)){
            $rows[] = $row[0];
        }        
    }    
    return $rows;
    
}

function splitRule(string $rule): array
{
    $pattern = "/(.*)(\sbags\scontain\s)([0-9a-z\,\s]+)/mi";
    preg_match($pattern, $rule, $matches);
    
    $content = [];
    
    foreach (explode(",", $matches[3]) as $elt) {
        $subpattern = "/(\d+)+\s(.*)\sbag[s]?/mi";
        preg_match($subpattern, trim($elt), $submatches);
        
        if (count($submatches) > 1) {
            $content[$submatches[2]] = $submatches[1]; //bag name => number contained
        }
    }
    
    return [trim($matches[1]), $content];
}

function getTree(): array{
    $tree = [];
    foreach (getInput() as $rule) {
        if(empty($rule)){
            continue;
        }
        list($bag, $content) = splitRule($rule);        
        $tree[$bag] = $content;
    }
    return $tree;
}

function part1(): int
{
    
    $tree = getTree();        
    
    $passed = [];
    $targets = [ MY_BAG ];
    $sum = 0;
    
    while(count($targets) > 0){
        $nextTargets = [];
        
        foreach($tree as $bag => $content){
            if(in_array($bag, $targets)){
                continue;
            }
            
            foreach($targets as $target){
                if(false === array_key_exists($target, $content)){
                    continue;
                }
                
                if(in_array($target, $passed) || in_array($bag, $passed)){
                    continue;
                }
                
                $nextTargets[] = $bag;
                $sum++;
                break;            
            }            
        }
    
        $passed = array_merge($passed, $targets);
        $targets = array_unique($nextTargets);  
    }
    return $sum;
}



function part2(): int
{
   return 0;
}

echo sprintf("result of part 1 is %d\n", part1());
echo sprintf("result of part 2 is %d\n", part2());