# Patriot CTF | Misc | Flower Shop
by warlock_merlin

## The Challenge

At first I thought it had to be a SQL injection, and I don't know PHP, but I know what a prepared statement is (from java), and the whole codebase was littered with them. I tried looking up php syntax as well to make sure they were using prepared statements correctly and although it was a little different from how other people do it online, it still looked secure enough to not be exploited. (Only thing you can do is % wildcard in a LIKE statement, but the code didn't have any LIKE statements in the SQL)

I also figured out quite early that you could trigger the password reset for other users quite easily, but I also learned that was a bust because each user gets their own webhook, and unless you can change their webhook to your own, you're not going to see the temp password.

While I was reading through the password reset logic I saw the exec statement that just concatenated some strings together to make a bash shell command. I didn't believe it could possibly be a shell injection, because I've never done that before, but I've written enough janky code to know that was janky. (And because you can tell they put flowershop in a docker container, so you would still be sandboxed so you can't break the ctf for other people.)

At first I thought it had to be a SQL injection, and I don't know PHP, but I know what a prepared statement is (from java), and the whole codebase was littered with them. I tried looking up php syntax as well to make sure they were using prepared statements correctly and although it was a little different from how other people do it online, it still looked secure enough to not be exploited. (Only thing you can do is `%` wildcard in a LIKE statement, but the code didn't have any LIKE statements in the SQL)

I also figured out quite early that you could trigger the password reset for other users quite easily, but I also learned that was a bust because each user gets their own webhook, and unless you can change their webhook to your own, you're not going to see the temp password.

While I was reading through the password reset logic I saw the exec statement that just concatenated some strings together to make a bash shell command. I didn't believe it could possibly be a shell injection, because I've never done that before, but I've written enough janky code to know that was janky. (And because you can tell they put flowershop in a docker container, so you would still be sandboxed so you can't break the ctf for other people.)

At first I thought it had to be a SQL injection, and I don't know PHP, but I know what a prepared statement is (from java), and the whole codebase was littered with them. I tried looking up php syntax as well to make sure they were using prepared statements correctly and although it was a little different from how other people do it online, it still looked secure enough to not be exploited. (Only thing you can do is `%` wildcard in a LIKE statement, but the code didn't have any LIKE statements in the SQL)

I also figured out quite early that you could trigger the password reset for other users quite easily, but I also learned that was a bust because each user gets their own webhook, and unless you can change their webhook to your own, you're not going to see the temp password.

While I was reading through the password reset logic I saw the exec statement that just concatenated some strings together to make a bash shell command. I didn't believe it could possibly be a shell injection, because I've never done that before, but I've written enough janky code to know that was janky. (And because you can tell they put flowershop in a docker container, so you would still be sandboxed so you can't break the ctf for other people.)

At first I thought it had to be a SQL injection, and I don't know PHP, but I know what a prepared statement is (from java), and the whole codebase was littered with them. I tried looking up php syntax as well to make sure they were using prepared statements correctly and although it was a little different from how other people do it online, it still looked secure enough to not be exploited. (Only thing you can do is `%` wildcard in a LIKE statement, but the code didn't have any LIKE statements in the SQL)

I also figured out quite early that you could trigger the password reset for other users quite easily, but I also learned that was a bust because each user gets their own webhook, and unless you can change their webhook to your own, you're not going to see the temp password.

While I was reading through the password reset logic I saw the exec statement that just concatenated some strings together to make a bash shell command. I didn't believe it could possibly be a shell injection, because I've never done that before, but I've written enough janky code to know that was janky. (And because you can tell they put flowershop in a docker container, so you would still be sandboxed so you can't break the ctf for other people.)
By this point, (from reading source code), I already knew that there was a filter on the webhook's input, (line 50 of `classes/signup.class.php`, `filter_var($wh, FILTER_SANITIZE_URL)`) so I looked up that filter: https://www.w3schools.com/php/filter_sanitize_url.asp
And it does next to nothing, it allows pretty much all special characters, and makes no attempt to actually resolve it as a url, pretty much all it does is remove whitespace.

So I Googled "alternative to whitespace bash" and found https://unix.stackexchange.com/questions/351331/how-to-send-a-command-with-arguments-without-spaces
It uses a variable substitution (duh!)

Still in disbelief that this would actually work, I tried just injecting `whoami` as the temp password to send back to me. (This has a double benefit since I've never seen a username with whitespace, so I knew it would be more likely to parse the way I expect)

And my `tmp_pass` sent this back to me:

`tmp_pass=www-data`

Winner winner chicken dinner!

Since they provide the entirety of flower shops source code so graciously, they actually show you exactly where the flag is stored (they even put a `CACI{FAKE_FLAG_FOR_TESTING}` Just to make it super clear where it is.)

So I know I can run arbitrary bash code, but in the interest of time I decided to just grab the flag. I tried to `cat` the whole `admin.php`, but nothing sent back, and it's because the file has whitespace and newlines so it messes up the bash arguments to the send_pass.php script. I'm glad I didn't try this more complex injection first because knowing me I would've just gotten discouraged and thought shell injection wasn't going to work. But luckily I already knew shell injection worked so I tried a different way.