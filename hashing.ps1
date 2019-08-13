Measure-Command { 
    Get-ChildItem -Path "C:\Windows\SysWOW64" -Recurse -ErrorAction SilentlyContinue -Force | 
        Get-FileHash -Algorithm SHA1
}

Get-ChildItem -Path "C:\Windows\SysWOW64" -Recurse -ErrorAction SilentlyContinue -Force | 
        Get-FileHash -Algorithm SHA1 | 
        Export-Csv C:\Users\re\Desktop\syswow64.csv

$re = Import-Csv C:\syswow64.csv
$work = Import-Csv C:\work_syswow64.csv

Compare-Object -ReferenceObject $re.Hash -DifferenceObject $work.Hash

$re_ht = @{}
foreach ($h in $re) {
    $re_ht[$h.Path] = $h.Hash
}

$re_ht.GetEnumerator() | Select -First 10

If ($re_ht.ContainsKey("C:\Windows\SysWOW64\12520437.cpx")) {Echo Ok}
If (!$re_ht.ContainsKey("wierd key")) {Echo "No wierd key"}

$work_hash_ht = @{}
foreach ($h in $work) {
    if (!$work_hash_ht.ContainsKey($h.Hash)){
        $work_hash_ht[$h.Hash] = @($h.Path)
    }
    else {
        $work_hash_ht[$h.Hash] += $h.Path
    }
}

$work_hash_ht.GetEnumerator() | Select -First 10
