[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [ValidateNotNullOrEmpty()]
    [string] $Prompt,

    [Parameter()]
    [ValidateNotNullOrEmpty()]
    [string] $Cwd = (Get-Location).Path,

    [Parameter()]
    [ValidateNotNullOrEmpty()]
    [string] $MaxTime = '20m',

    [Parameter()]
    [switch] $KeepSession
)

$ErrorActionPreference = 'Stop'

$omp = @(Get-Command 'omp' -CommandType Application -ErrorAction Stop)[0]
$resolvedCwd = (Resolve-Path -LiteralPath $Cwd -ErrorAction Stop).Path

$ompArgs = @(
    '-p'
    '--model', 'openai-codex/gpt-5.6-luna'
    '--thinking', 'medium'
    '--approval-mode', 'yolo'
    '--auto-approve'
    '--cwd', $resolvedCwd
    '--max-time', $MaxTime
)

if (-not $KeepSession) {
    $ompArgs += '--no-session'
}

$ompArgs += $Prompt

& $omp.Source @ompArgs
if ($LASTEXITCODE -ne 0) {
    throw "OMP delegate failed with exit code $LASTEXITCODE."
}
