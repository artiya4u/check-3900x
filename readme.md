# Check 3900X
Bot to notify when Ryzen 3900X out in Thailand online store (J.I.B., Advice)

## Usage
- Clone this project `git clone https://github.com/artiya4u/check-3900x.git` and `run pip3 -r requirements.txt`
- Get LINE notify `TOKEN` at https://notify-bot.line.me/my/ and change it it `notification.py`
- Set crontab on Linux (`crontab -e`) to run every minute like this
```crontab
*/1 * * * * cd check-3900x && python3 check.py &>> RYZEN3900x.log
```