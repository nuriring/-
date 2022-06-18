```js
const date = new Date()
const year = 2000
const month = 1

var days = null

const arr = [31, [29, 28], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


if (month === 1) {
  if((year % 4 == 0) && (year % 100 != 0) || (year % 400) == 0)
      days = arr[1][0];
    else
      days = arr[1][1];
} else {
  days = arr[month]
}

console.log(days + ' days for ' + year + '-' + (month + 1))
```

