while($true) {
    git add .
    git commit -m "auto-sync"
    git push origin main
    Start-Sleep -Seconds 60
}