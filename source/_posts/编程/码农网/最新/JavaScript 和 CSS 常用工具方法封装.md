
---
title: 'JavaScript 和 CSS 常用工具方法封装'
categories: 
 - 编程
 - 码农网
 - 最新
headimg: 'https://picsum.photos/400/300?random=3166'
author: 码农网
comments: false
date: Thu, 21 Feb 2019 12:42:04 GMT
thumbnail: 'https://picsum.photos/400/300?random=3166'
---

<div>   
<blockquote><p>因为工作中经常用到这些方法，所有便把这些方法进行了总结。</p></blockquote>
<h2 id="articleHeader0">JavaScript</h2>
<h3>1. type 类型判断</h3>
<pre class="brush: javascript; gutter: true; first-line: 1">isString (o) &#123; //是否字符串
    return Object.prototype.toString.call(o).slice(8, -1) === 'String'
&#125;

isNumber (o) &#123; //是否数字
    return Object.prototype.toString.call(o).slice(8, -1) === 'Number'
&#125;

isBoolean (o) &#123; //是否boolean
    return Object.prototype.toString.call(o).slice(8, -1) === 'Boolean'
&#125;

isFunction (o) &#123; //是否函数
    return Object.prototype.toString.call(o).slice(8, -1) === 'Function'
&#125;

isNull (o) &#123; //是否为null
    return Object.prototype.toString.call(o).slice(8, -1) === 'Null'
&#125;

isUndefined (o) &#123; //是否undefined
    return Object.prototype.toString.call(o).slice(8, -1) === 'Undefined'
&#125;

isObj (o) &#123; //是否对象
    return Object.prototype.toString.call(o).slice(8, -1) === 'Object'
&#125;

isArray (o) &#123; //是否数组
    return Object.prototype.toString.call(o).slice(8, -1) === 'Array'
&#125;

isDate (o) &#123; //是否时间
    return Object.prototype.toString.call(o).slice(8, -1) === 'Date'
&#125;

isRegExp (o) &#123; //是否正则
    return Object.prototype.toString.call(o).slice(8, -1) === 'RegExp'
&#125;

isError (o) &#123; //是否错误对象
    return Object.prototype.toString.call(o).slice(8, -1) === 'Error'
&#125;

isSymbol (o) &#123; //是否Symbol函数
    return Object.prototype.toString.call(o).slice(8, -1) === 'Symbol'
&#125;

isPromise (o) &#123; //是否Promise对象
    return Object.prototype.toString.call(o).slice(8, -1) === 'Promise'
&#125;

isSet (o) &#123; //是否Set对象
    return Object.prototype.toString.call(o).slice(8, -1) === 'Set'
&#125;

isFalse (o) &#123;
    if (!o || o === 'null' || o === 'undefined' || o === 'false' || o === 'NaN') return true
        return false
&#125;

isTrue (o) &#123;
    return !this.isFalse(o)
&#125;

isIos () &#123;
    var u = navigator.userAgent;
    if (u.indexOf('Android') > -1 || u.indexOf('Linux') > -1) &#123;//安卓手机
        // return "Android";
        return false
    &#125; else if (u.indexOf('iPhone') > -1) &#123;//苹果手机
        // return "iPhone";
        return true
    &#125; else if (u.indexOf('iPad') > -1) &#123;//iPad
        // return "iPad";
        return false
    &#125; else if (u.indexOf('Windows Phone') > -1) &#123;//winphone手机
        // return "Windows Phone";
        return false
    &#125;else&#123;
        return false
    &#125;
&#125;

isPC () &#123; //是否为PC端
    var userAgentInfo = navigator.userAgent;
    var Agents = ["Android", "iPhone",
                "SymbianOS", "Windows Phone",
                "iPad", "iPod"];
    var flag = true;
    for (var v = 0; v < Agents.length; v++) &#123;
        if (userAgentInfo.indexOf(Agents[v]) > 0) &#123;
            flag = false;
            break;
        &#125;
    &#125;
    return flag;
&#125;

browserType()&#123;
    var userAgent = navigator.userAgent; //取得浏览器的userAgent字符串
    var isOpera = userAgent.indexOf("Opera") > -1; //判断是否Opera浏览器
    var isIE = userAgent.indexOf("compatible") > -1 && userAgent.indexOf("MSIE") > -1 && !isOpera; //判断是否IE浏览器
    var isIE11 = userAgent.indexOf('Trident') > -1 && userAgent.indexOf("rv:11.0") > -1;
    var isEdge = userAgent.indexOf("Edge") > -1 && !isIE; //判断是否IE的Edge浏览器  
    var isFF = userAgent.indexOf("Firefox") > -1; //判断是否Firefox浏览器
    var isSafari = userAgent.indexOf("Safari") > -1 && userAgent.indexOf("Chrome") == -1; //判断是否Safari浏览器
    var isChrome = userAgent.indexOf("Chrome") > -1 && userAgent.indexOf("Safari") > -1; //判断Chrome浏览器

    if (isIE) &#123;
        var reIE = new RegExp("MSIE (\\d+\\.\\d+);");
        reIE.test(userAgent);
        var fIEVersion = parseFloat(RegExp["$1"]);
        if(fIEVersion == 7) return "IE7"
        else if(fIEVersion == 8) return "IE8";
        else if(fIEVersion == 9) return "IE9";
        else if(fIEVersion == 10) return "IE10";
        else return "IE7以下"//IE版本过低
    &#125;
    if (isIE11) return 'IE11';
    if (isEdge) return "Edge";
    if (isFF) return "FF";
    if (isOpera) return "Opera";
    if (isSafari) return "Safari";
    if (isChrome) return "Chrome";
&#125;

checkStr (str, type) &#123;
    switch (type) &#123;
        case 'phone':   //手机号码
            return /^1[3|4|5|6|7|8|9][0-9]&#123;9&#125;$/.test(str);
        case 'tel':     //座机
            return /^(0\d&#123;2,3&#125;-\d&#123;7,8&#125;)(-\d&#123;1,4&#125;)?$/.test(str);
        case 'card':    //身份证
            return /(^\d&#123;15&#125;$)|(^\d&#123;18&#125;$)|(^\d&#123;17&#125;(\d|X|x)$)/.test(str);
        case 'pwd':     //密码以字母开头，长度在6~18之间，只能包含字母、数字和下划线
            return /^[a-zA-Z]\w&#123;5,17&#125;$/.test(str)
        case 'postal':  //邮政编码
            return /[1-9]\d&#123;5&#125;(?!\d)/.test(str);
        case 'QQ':      //QQ号
            return /^[1-9][0-9]&#123;4,9&#125;$/.test(str);
        case 'email':   //邮箱
            return /^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$/.test(str);
        case 'money':   //金额(小数点2位)
            return /^\d*(?:\.\d&#123;0,2&#125;)?$/.test(str);
        case 'URL':     //网址
            return /(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?/.test(str)
        case 'IP':      //IP
            return /((?:(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d)\\.)&#123;3&#125;(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d))/.test(str);
        case 'date':    //日期时间
            return /^(\d&#123;4&#125;)\-(\d&#123;2&#125;)\-(\d&#123;2&#125;) (\d&#123;2&#125;)(?:\:\d&#123;2&#125;|:(\d&#123;2&#125;):(\d&#123;2&#125;))$/.test(str) || /^(\d&#123;4&#125;)\-(\d&#123;2&#125;)\-(\d&#123;2&#125;)$/.test(str)
        case 'number':  //数字
            return /^[0-9]$/.test(str);
        case 'english': //英文
            return /^[a-zA-Z]+$/.test(str);
        case 'chinese': //中文
            return /^[\u4E00-\u9FA5]+$/.test(str);
        case 'lower':   //小写
            return /^[a-z]+$/.test(str);
        case 'upper':   //大写
            return /^[A-Z]+$/.test(str);
        case 'HTML':    //HTML标记
            return /<("[^"]*"|'[^']*'|[^'">])*>/.test(str);
        default:
            return true;
    &#125;

    // 严格的身份证校验
    isCardID(sId) &#123;
        if (!/(^\d&#123;15&#125;$)|(^\d&#123;17&#125;(\d|X|x)$)/.test(sId)) &#123;
            alert('你输入的身份证长度或格式错误')
            return false
        &#125;
        //身份证城市
        var aCity=&#123;11:"北京",12:"天津",13:"河北",14:"山西",15:"内蒙古",21:"辽宁",22:"吉林",23:"黑龙江",31:"上海",32:"江苏",33:"浙江",34:"安徽",35:"福建",36:"江西",37:"山东",41:"河南",42:"湖北",43:"湖南",44:"广东",45:"广西",46:"海南",50:"重庆",51:"四川",52:"贵州",53:"云南",54:"西藏",61:"陕西",62:"甘肃",63:"青海",64:"宁夏",65:"新疆",71:"台湾",81:"香港",82:"澳门",91:"国外"&#125;;
        if(!aCity[parseInt(sId.substr(0,2))]) &#123; 
            alert('你的身份证地区非法')
            return false
        &#125;

        // 出生日期验证
        var sBirthday=(sId.substr(6,4)+"-"+Number(sId.substr(10,2))+"-"+Number(sId.substr(12,2))).replace(/-/g,"/"),
            d = new Date(sBirthday)
        if(sBirthday != (d.getFullYear()+"/"+ (d.getMonth()+1) + "/" + d.getDate())) &#123;
            alert('身份证上的出生日期非法')
            return false
        &#125;

        // 身份证号码校验
        var sum = 0,
            weights =  [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2],
            codes = "10X98765432"
        for (var i = 0; i < sId.length - 1; i++) &#123;
            sum += sId[i] * weights[i];
        &#125;
        var last = codes[sum % 11]; //计算出来的最后一位身份证号码
        if (sId[sId.length-1] != last) &#123; 
            alert('你输入的身份证号非法')
            return false
        &#125;

        return true
    &#125;
&#125;</pre>
<h3>2. Date</h3>
<pre class="brush: javascript; gutter: true; first-line: 1">/**
 * 格式化时间
 * 
 * @param  &#123;time&#125; 时间
 * @param  &#123;cFormat&#125; 格式
 * @return &#123;String&#125; 字符串
 *
 * @example formatTime('2018-1-29', '&#123;y&#125;/&#123;m&#125;/&#123;d&#125; &#123;h&#125;:&#123;i&#125;:&#123;s&#125;') // -> 2018/01/29 00:00:00
 */
formatTime(time, cFormat) &#123;
    if (arguments.length === 0) return null
    if ((time + '').length === 10) &#123;
        time = +time * 1000
    &#125;

    var format = cFormat || '&#123;y&#125;-&#123;m&#125;-&#123;d&#125; &#123;h&#125;:&#123;i&#125;:&#123;s&#125;', date
    if (typeof time === 'object') &#123;
        date = time
    &#125; else &#123;
        date = new Date(time)
    &#125;

    var formatObj = &#123;
        y: date.getFullYear(),
        m: date.getMonth() + 1,
        d: date.getDate(),
        h: date.getHours(),
        i: date.getMinutes(),
        s: date.getSeconds(),
        a: date.getDay()
    &#125;
    var time_str = format.replace(/&#123;(y|m|d|h|i|s|a)+&#125;/g, (result, key) => &#123;
        var value = formatObj[key]
        if (key === 'a') return ['一', '二', '三', '四', '五', '六', '日'][value - 1]
        if (result.length > 0 && value < 10) &#123;
            value = '0' + value
        &#125;
        return value || 0
    &#125;)
    return time_str
&#125;

/**
 * 返回指定长度的月份集合
 * 
 * @param  &#123;time&#125; 时间
 * @param  &#123;len&#125; 长度
 * @param  &#123;direction&#125; 方向：  1: 前几个月;  2: 后几个月;  3:前后几个月  默认 3
 * @return &#123;Array&#125; 数组
 * 
 * @example   getMonths('2018-1-29', 6, 1)  // ->  ["2018-1", "2017-12", "2017-11", "2017-10", "2017-9", "2017-8", "2017-7"]
 */
getMonths(time, len, direction) &#123;
    var mm = new Date(time).getMonth(),
        yy = new Date(time).getFullYear(),
        direction = isNaN(direction) ? 3 : direction,
        index = mm;
    var cutMonth = function(index) &#123;
        if ( index <= len && index >= -len) &#123;
            return direction === 1 ? formatPre(index).concat(cutMonth(++index)):
                direction === 2 ? formatNext(index).concat(cutMonth(++index)):formatCurr(index).concat(cutMonth(++index))
        &#125;
        return []
    &#125;
    var formatNext = function(i) &#123;
        var y = Math.floor(i/12),
            m = i%12
        return [yy+y + '-' + (m+1)]
    &#125;
    var formatPre = function(i) &#123;
        var y = Math.ceil(i/12),
            m = i%12
        m = m===0 ? 12 : m
        return [yy-y + '-' + (13 - m)]
    &#125;
    var formatCurr = function(i) &#123;
        var y = Math.floor(i/12),
            yNext = Math.ceil(i/12),
            m = i%12,
            mNext = m===0 ? 12 : m
        return [yy-yNext + '-' + (13 - mNext),yy+y + '-' + (m+1)]
    &#125;
    // 数组去重
    var unique = function(arr) &#123;
        if ( Array.hasOwnProperty('from') ) &#123;
            return Array.from(new Set(arr));
        &#125;else&#123;
            var n = &#123;&#125;,r=[]; 
            for(var i = 0; i < arr.length; i++)&#123;
                if (!n[arr[i]])&#123;
                    n[arr[i]] = true; 
                    r.push(arr[i]);
                &#125;
            &#125;
            return r;
        &#125;
    &#125;
    return direction !== 3 ? cutMonth(index) : unique(cutMonth(index).sort(function(t1, t2)&#123;
        return new Date(t1).getTime() - new Date(t2).getTime()
    &#125;))
&#125;

/**
 * 返回指定长度的天数集合
 * 
 * @param  &#123;time&#125; 时间
 * @param  &#123;len&#125; 长度
 * @param  &#123;direction&#125; 方向： 1: 前几天;  2: 后几天;  3:前后几天  默认 3
 * @return &#123;Array&#125; 数组
 *
 * @example date.getDays('2018-1-29', 6) // -> ["2018-1-26", "2018-1-27", "2018-1-28", "2018-1-29", "2018-1-30", "2018-1-31", "2018-2-1"]
 */
getDays(time, len, diretion) &#123;
    var tt = new Date(time)
    var getDay = function(day) &#123;
        var t = new Date(time)
        t.setDate(t.getDate() + day)
        var m = t.getMonth()+1
        return t.getFullYear()+'-'+m+'-'+t.getDate()
    &#125;
    var arr = []
    if (diretion === 1) &#123;
        for (var i = 1; i <= len; i++) &#123;
            arr.unshift(getDay(-i))
        &#125;
    &#125;else if(diretion === 2) &#123;
        for (var i = 1; i <= len; i++) &#123;
            arr.push(getDay(i))
        &#125;
    &#125;else &#123;
        for (var i = 1; i <= len; i++) &#123;
            arr.unshift(getDay(-i))
        &#125;
        arr.push(tt.getFullYear()+'-'+(tt.getMonth()+1)+'-'+tt.getDate())
        for (var i = 1; i <= len; i++) &#123;
            arr.push(getDay(i))
        &#125;
    &#125;
    return diretion === 1 ? arr.concat([tt.getFullYear()+'-'+(tt.getMonth()+1)+'-'+tt.getDate()]) : 
        diretion === 2 ? [tt.getFullYear()+'-'+(tt.getMonth()+1)+'-'+tt.getDate()].concat(arr) : arr
&#125;

/**
 * @param  &#123;s&#125; 秒数
 * @return &#123;String&#125; 字符串 
 *
 * @example formatHMS(3610) // -> 1h0m10s
 */
formatHMS (s) &#123;
    var str = ''
    if (s > 3600) &#123;
        str = Math.floor(s/3600)+'h'+Math.floor(s%3600/60)+'m'+s%60+'s'
    &#125;else if(s > 60) &#123;
        str = Math.floor(s/60)+'m'+s%60+'s'
    &#125;else&#123;
        str = s%60+'s'
    &#125;
    return str
&#125;

/*获取某月有多少天*/
getMonthOfDay (time) &#123;
    var date = new Date(time)
    var year = date.getFullYear()
    var mouth = date.getMonth() + 1
    var days

    //当月份为二月时，根据闰年还是非闰年判断天数
    if (mouth == 2) &#123;
        days = (year%4==0 && year%100==0 && year%400==0) || (year%4==0 && year%100!=0) ? 28 : 29
    &#125; else if (mouth == 1 || mouth == 3 || mouth == 5 || mouth == 7 || mouth == 8 || mouth == 10 || mouth == 12) &#123;
        //月份为：1,3,5,7,8,10,12 时，为大月.则天数为31；
        days = 31
    &#125; else &#123;
        //其他月份，天数为：30.
        days = 30
    &#125;
    return days
&#125;

/*获取某年有多少天*/
getYearOfDay (time) &#123;
    var firstDayYear = this.getFirstDayOfYear(time);
    var lastDayYear = this.getLastDayOfYear(time);
    var numSecond = (new Date(lastDayYear).getTime() - new Date(firstDayYear).getTime())/1000;
    return Math.ceil(numSecond/(24*3600));
&#125;

/*获取某年的第一天*/
getFirstDayOfYear (time) &#123;
    var year = new Date(time).getFullYear();
    return year + "-01-01 00:00:00";
&#125;

/*获取某年最后一天*/
getLastDayOfYear (time) &#123;
    var year = new Date(time).getFullYear();
    var dateString = year + "-12-01 00:00:00";
    var endDay = this.getMonthOfDay(dateString);
    return year + "-12-" + endDay + " 23:59:59";
&#125;

/*获取某个日期是当年中的第几天*/
getDayOfYear (time) &#123;
    var firstDayYear = this.getFirstDayOfYear(time);
    var numSecond = (new Date(time).getTime() - new Date(firstDayYear).getTime())/1000;
    return Math.ceil(numSecond/(24*3600));
&#125;

/*获取某个日期在这一年的第几周*/
getDayOfYearWeek (time) &#123;
    var numdays = this.getDayOfYear(time);
    return Math.ceil(numdays / 7);
&#125;</pre>
<h3>3. Array</h3>
<pre class="brush: javascript; gutter: true; first-line: 1">/*判断一个元素是否在数组中*/
contains (arr, val) &#123;
    return arr.indexOf(val) != -1 ? true : false;
&#125;

/**
 * @param  &#123;arr&#125; 数组
 * @param  &#123;fn&#125; 回调函数
 * @return &#123;undefined&#125;
 */
each (arr, fn) &#123;
    fn = fn || Function;
    var a = [];
    var args = Array.prototype.slice.call(arguments, 1);
    for(var i = 0; i < arr.length; i++) &#123;
        var res = fn.apply(arr, [arr[i], i].concat(args));
        if(res != null) a.push(res);
    &#125;
&#125;

/**
 * @param  &#123;arr&#125; 数组
 * @param  &#123;fn&#125; 回调函数
 * @param  &#123;thisObj&#125; this指向
 * @return &#123;Array&#125; 
 */
map (arr, fn, thisObj) &#123;
    var scope = thisObj || window;
    var a = [];
    for(var i = 0, j = arr.length; i < j; ++i) &#123;
        var res = fn.call(scope, arr[i], i, this);
        if(res != null) a.push(res);
    &#125;
    return a;
&#125;

/**
 * @param  &#123;arr&#125; 数组
 * @param  &#123;type&#125; 1：从小到大   2：从大到小   3：随机
 * @return &#123;Array&#125;
 */
sort (arr, type = 1) &#123;
    return arr.sort( (a, b) => &#123;
        switch(type) &#123;
            case 1:
                return a - b;
            case 2:
                return b - a;
            case 3:
                return Math.random() - 0.5;
            default:
                return arr;
        &#125;
    &#125;)
&#125;

/*去重*/
unique (arr) &#123;
    if ( Array.hasOwnProperty('from') ) &#123;
        return Array.from(new Set(arr));
    &#125;else&#123;
        var n = &#123;&#125;,r=[]; 
        for(var i = 0; i < arr.length; i++)&#123;
            if (!n[arr[i]])&#123;
                n[arr[i]] = true; 
                r.push(arr[i]);
            &#125;
        &#125;
        return r;
    &#125;
    // 注：上面 else 里面的排重并不能区分 2 和 '2'，但能减少用indexOf带来的性能,暂时没找到替代的方法。。。
    /* 正确排重
    if ( Array.hasOwnProperty('from') ) &#123;
        return Array.from(new Set(arr))
    &#125;else&#123;
        var r = [], NaNBol = true
        for(var i=0; i < arr.length; i++) &#123;
            if (arr[i] !== arr[i]) &#123;
                if (NaNBol && r.indexOf(arr[i]) === -1) &#123;
                    r.push(arr[i])
                    NaNBol = false
                &#125;
            &#125;else&#123;
                if(r.indexOf(arr[i]) === -1) r.push(arr[i])
            &#125;
        &#125;
        return r
    &#125;

     */
&#125;

/*求两个集合的并集*/
union (a, b) &#123;
    var newArr = a.concat(b);
    return this.unique(newArr);
&#125;

/*求两个集合的交集*/
intersect (a, b) &#123;
    var _this = this;
    a = this.unique(a);
    return this.map(a, function(o) &#123;
        return _this.contains(b, o) ? o : null;
    &#125;);
&#125;

/*删除其中一个元素*/
remove (arr, ele) &#123;
    var index = arr.indexOf(ele);
    if(index > -1) &#123;
        arr.splice(index, 1);
    &#125;
    return arr;
&#125;

/*将类数组转换为数组的方法*/
formArray (ary) &#123;
    var arr = [];
    if(Array.isArray(ary)) &#123;
        arr = ary;
    &#125; else &#123;
        arr = Array.prototype.slice.call(ary);
    &#125;;
    return arr;
&#125;

/*最大值*/
max (arr) &#123;
    return Math.max.apply(null, arr);
&#125;

/*最小值*/
min (arr) &#123;
    return Math.min.apply(null, arr);
&#125;

/*求和*/
sum (arr) &#123;
    return arr.reduce( (pre, cur) => &#123;
        return pre + cur
    &#125;)
&#125;

/*平均值*/
average (arr) &#123;
    return this.sum(arr)/arr.length
&#125;</pre>
<h3>4. String 字符串操作</h3>
<pre class="brush: javascript; gutter: true; first-line: 1">/**
 * 去除空格
 * @param  &#123;str&#125;
 * @param  &#123;type&#125; 
 *       type:  1-所有空格  2-前后空格  3-前空格 4-后空格
 * @return &#123;String&#125;
 */
trim (str, type) &#123;
    type = type || 1
    switch (type) &#123;
        case 1:
            return str.replace(/\s+/g, "");
        case 2:
            return str.replace(/(^\s*)|(\s*$)/g, "");
        case 3:
            return str.replace(/(^\s*)/g, "");
        case 4:
            return str.replace(/(\s*$)/g, "");
        default:
            return str;
    &#125;
&#125;

/**
 * @param  &#123;str&#125; 
 * @param  &#123;type&#125;
 *       type:  1:首字母大写  2：首页母小写  3：大小写转换  4：全部大写  5：全部小写
 * @return &#123;String&#125;
 */
changeCase (str, type) &#123;
    type = type || 4
    switch (type) &#123;
        case 1:
            return str.replace(/\b\w+\b/g, function (word) &#123;
                return word.substring(0, 1).toUpperCase() + word.substring(1).toLowerCase();

            &#125;);
        case 2:
            return str.replace(/\b\w+\b/g, function (word) &#123;
                return word.substring(0, 1).toLowerCase() + word.substring(1).toUpperCase();
            &#125;);
        case 3:
            return str.split('').map( function(word)&#123;
                if (/[a-z]/.test(word)) &#123;
                    return word.toUpperCase();
                &#125;else&#123;
                    return word.toLowerCase()
                &#125;
            &#125;).join('')
        case 4:
            return str.toUpperCase();
        case 5:
            return str.toLowerCase();
        default:
            return str;
    &#125;
&#125;

/*
    检测密码强度
*/
checkPwd (str) &#123;
    var Lv = 0;
    if (str.length < 6) &#123;
        return Lv
    &#125;
    if (/[0-9]/.test(str)) &#123;
        Lv++
    &#125;
    if (/[a-z]/.test(str)) &#123;
        Lv++
    &#125;
    if (/[A-Z]/.test(str)) &#123;
        Lv++
    &#125;
    if (/[\.|-|_]/.test(str)) &#123;
        Lv++
    &#125;
    return Lv;
&#125;

/*过滤html代码(把<>转换)*/
filterTag (str) &#123;
    str = str.replace(/&/ig, "&amp;");
    str = str.replace(/</ig, "&lt;");
    str = str.replace(/>/ig, "&gt;");
    str = str.replace(" ", " ");
    return str;
&#125;</pre>
<h3>5. Number</h3>
<pre class="brush: javascript; gutter: true; first-line: 1">/*随机数范围*/
random (min, max) &#123;
    if (arguments.length === 2) &#123;
        return Math.floor(min + Math.random() * ( (max+1) - min ))
    &#125;else&#123;
        return null;
    &#125;

&#125;

/*将阿拉伯数字翻译成中文的大写数字*/
numberToChinese (num) &#123;
    var AA = new Array("零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十");
    var BB = new Array("", "十", "百", "仟", "萬", "億", "点", "");
    var a = ("" + num).replace(/(^0*)/g, "").split("."),
        k = 0,
        re = "";
    for(var i = a[0].length - 1; i >= 0; i--) &#123;
        switch(k) &#123;
            case 0:
                re = BB[7] + re;
                break;
            case 4:
                if(!new RegExp("0&#123;4&#125;//d&#123;" + (a[0].length - i - 1) + "&#125;$")
                    .test(a[0]))
                    re = BB[4] + re;
                break;
            case 8:
                re = BB[5] + re;
                BB[7] = BB[5];
                k = 0;
                break;
        &#125;
        if(k % 4 == 2 && a[0].charAt(i + 2) != 0 && a[0].charAt(i + 1) == 0)
            re = AA[0] + re;
        if(a[0].charAt(i) != 0)
            re = AA[a[0].charAt(i)] + BB[k % 4] + re;
        k++;
    &#125;

    if(a.length > 1) // 加上小数部分(如果有小数部分)
    &#123;
        re += BB[6];
        for(var i = 0; i < a[1].length; i++)
            re += AA[a[1].charAt(i)];
    &#125;
    if(re == '一十')
        re = "十";
    if(re.match(/^一/) && re.length == 3)
        re = re.replace("一", "");
    return re;
&#125;

/*将数字转换为大写金额*/
changeToChinese (Num) &#123;
        //判断如果传递进来的不是字符的话转换为字符
        if(typeof Num == "number") &#123;
            Num = new String(Num);
        &#125;;
        Num = Num.replace(/,/g, "") //替换tomoney()中的“,”
        Num = Num.replace(/ /g, "") //替换tomoney()中的空格
        Num = Num.replace(/￥/g, "") //替换掉可能出现的￥字符
        if(isNaN(Num)) &#123; //验证输入的字符是否为数字
            //alert("请检查小写金额是否正确");
            return "";
        &#125;;
        //字符处理完毕后开始转换，采用前后两部分分别转换
        var part = String(Num).split(".");
        var newchar = "";
        //小数点前进行转化
        for(var i = part[0].length - 1; i >= 0; i--) &#123;
            if(part[0].length > 10) &#123;
                return "";
                //若数量超过拾亿单位，提示
            &#125;
            var tmpnewchar = ""
            var perchar = part[0].charAt(i);
            switch(perchar) &#123;
                case "0":
                    tmpnewchar = "零" + tmpnewchar;
                    break;
                case "1":
                    tmpnewchar = "壹" + tmpnewchar;
                    break;
                case "2":
                    tmpnewchar = "贰" + tmpnewchar;
                    break;
                case "3":
                    tmpnewchar = "叁" + tmpnewchar;
                    break;
                case "4":
                    tmpnewchar = "肆" + tmpnewchar;
                    break;
                case "5":
                    tmpnewchar = "伍" + tmpnewchar;
                    break;
                case "6":
                    tmpnewchar = "陆" + tmpnewchar;
                    break;
                case "7":
                    tmpnewchar = "柒" + tmpnewchar;
                    break;
                case "8":
                    tmpnewchar = "捌" + tmpnewchar;
                    break;
                case "9":
                    tmpnewchar = "玖" + tmpnewchar;
                    break;
            &#125;
            switch(part[0].length - i - 1) &#123;
                case 0:
                    tmpnewchar = tmpnewchar + "元";
                    break;
                case 1:
                    if(perchar != 0) tmpnewchar = tmpnewchar + "拾";
                    break;
                case 2:
                    if(perchar != 0) tmpnewchar = tmpnewchar + "佰";
                    break;
                case 3:
                    if(perchar != 0) tmpnewchar = tmpnewchar + "仟";
                    break;
                case 4:
                    tmpnewchar = tmpnewchar + "万";
                    break;
                case 5:
                    if(perchar != 0) tmpnewchar = tmpnewchar + "拾";
                    break;
                case 6:
                    if(perchar != 0) tmpnewchar = tmpnewchar + "佰";
                    break;
                case 7:
                    if(perchar != 0) tmpnewchar = tmpnewchar + "仟";
                    break;
                case 8:
                    tmpnewchar = tmpnewchar + "亿";
                    break;
                case 9:
                    tmpnewchar = tmpnewchar + "拾";
                    break;
            &#125;
            var newchar = tmpnewchar + newchar;
        &#125;
        //小数点之后进行转化
        if(Num.indexOf(".") != -1) &#123;
            if(part[1].length > 2) &#123;
                // alert("小数点之后只能保留两位,系统将自动截断");
                part[1] = part[1].substr(0, 2)
            &#125;
            for(i = 0; i < part[1].length; i++) &#123;
                tmpnewchar = ""
                perchar = part[1].charAt(i)
                switch(perchar) &#123;
                    case "0":
                        tmpnewchar = "零" + tmpnewchar;
                        break;
                    case "1":
                        tmpnewchar = "壹" + tmpnewchar;
                        break;
                    case "2":
                        tmpnewchar = "贰" + tmpnewchar;
                        break;
                    case "3":
                        tmpnewchar = "叁" + tmpnewchar;
                        break;
                    case "4":
                        tmpnewchar = "肆" + tmpnewchar;
                        break;
                    case "5":
                        tmpnewchar = "伍" + tmpnewchar;
                        break;
                    case "6":
                        tmpnewchar = "陆" + tmpnewchar;
                        break;
                    case "7":
                        tmpnewchar = "柒" + tmpnewchar;
                        break;
                    case "8":
                        tmpnewchar = "捌" + tmpnewchar;
                        break;
                    case "9":
                        tmpnewchar = "玖" + tmpnewchar;
                        break;
                &#125;
                if(i == 0) tmpnewchar = tmpnewchar + "角";
                if(i == 1) tmpnewchar = tmpnewchar + "分";
                newchar = newchar + tmpnewchar;
            &#125;
        &#125;
        //替换所有无用汉字
        while(newchar.search("零零") != -1)
            newchar = newchar.replace("零零", "零");
        newchar = newchar.replace("零亿", "亿");
        newchar = newchar.replace("亿万", "亿");
        newchar = newchar.replace("零万", "万");
        newchar = newchar.replace("零元", "元");
        newchar = newchar.replace("零角", "");
        newchar = newchar.replace("零分", "");
        if(newchar.charAt(newchar.length - 1) == "元") &#123;
            newchar = newchar + "整"
        &#125;
        return newchar;
    &#125;</pre>
<h3>6. Http</h3>
<pre class="brush: javascript; gutter: true; first-line: 1">/**
 * @param  &#123;setting&#125;
 */
ajax(setting)&#123;
    //设置参数的初始值
    var opts=&#123;
        method: (setting.method || "GET").toUpperCase(), //请求方式
        url: setting.url || "", // 请求地址
        async: setting.async || true, // 是否异步
        dataType: setting.dataType || "json", // 解析方式
        data: setting.data || "", // 参数
        success: setting.success || function()&#123;&#125;, // 请求成功回调
        error: setting.error || function()&#123;&#125; // 请求失败回调
    &#125;

    // 参数格式化
    function params_format (obj) &#123;
        var str = ''
        for (var i in obj) &#123;
            str += i + '=' + obj[i] + '&'
        &#125;
        return str.split('').slice(0, -1).join('')
    &#125;

    // 创建ajax对象
    var xhr=new XMLHttpRequest();

    // 连接服务器open(方法GET/POST，请求地址， 异步传输)
    if(opts.method == 'GET')&#123;
        xhr.open(opts.method, opts.url + "?" + params_format(opts.data), opts.async);
        xhr.send();
    &#125;else&#123;
        xhr.open(opts.method, opts.url, opts.async);
        xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
        xhr.send(opts.data);
    &#125;

    /*
    ** 每当readyState改变时，就会触发onreadystatechange事件
    ** readyState属性存储有XMLHttpRequest的状态信息
    ** 0 ：请求未初始化
    ** 1 ：服务器连接已建立
    ** 2 ：请求已接受
    ** 3 : 请求处理中
    ** 4 ：请求已完成，且相应就绪
    */
    xhr.onreadystatechange = function() &#123;
        if (xhr.readyState === 4 && (xhr.status === 200 || xhr.status === 304)) &#123;
            switch(opts.dataType)&#123;
                case "json":
                    var json = JSON.parse(xhr.responseText);
                    opts.success(json);
                    break;
                case "xml":
                    opts.success(xhr.responseXML);
                    break;
                default:
                    opts.success(xhr.responseText);
                    break;
            &#125;
        &#125;
    &#125;

    xhr.onerror = function(err) &#123;
        opts.error(err);
    &#125;
&#125;

/**
 * @param  &#123;url&#125;
 * @param  &#123;setting&#125;
 * @return &#123;Promise&#125;
 */
fetch(url, setting) &#123;
    //设置参数的初始值
    let opts=&#123;
        method: (setting.method || 'GET').toUpperCase(), //请求方式
        headers : setting.headers  || &#123;&#125;, // 请求头设置
        credentials : setting.credentials  || true, // 设置cookie是否一起发送
        body: setting.body || &#123;&#125;,
        mode : setting.mode  || 'no-cors', // 可以设置 cors, no-cors, same-origin
        redirect : setting.redirect  || 'follow', // follow, error, manual
        cache : setting.cache  || 'default' // 设置 cache 模式 (default, reload, no-cache)
    &#125;
    let dataType = setting.dataType || "json", // 解析方式  
        data = setting.data || "" // 参数

    // 参数格式化
    function params_format (obj) &#123;
        var str = ''
        for (var i in obj) &#123;
            str += `$&#123;i&#125;=$&#123;obj[i]&#125;&`
        &#125;
        return str.split('').slice(0, -1).join('')
    &#125;

    if (opts.method === 'GET') &#123;
        url = url + (data?`?$&#123;params_format(data)&#125;`:'')
    &#125;else&#123;
        setting.body = data || &#123;&#125;
    &#125;

    return new Promise( (resolve, reject) => &#123;
        fetch(url, opts).then( async res => &#123;
            let data = dataType === 'text' ? await res.text() :
                dataType === 'blob' ? await res.blob() : await res.json() 
            resolve(data)
        &#125;).catch( e => &#123;
            reject(e)
        &#125;)
    &#125;)

&#125;</pre>
<h3>7. DOM</h3>
<pre class="brush: javascript; gutter: true; first-line: 1">$ (selector)&#123; 
    var type = selector.substring(0, 1);
    if (type === '#') &#123;
        if (document.querySelecotor) return document.querySelector(selector)
            return document.getElementById(selector.substring(1))

    &#125;else if (type === '.') &#123;
        if (document.querySelecotorAll) return document.querySelectorAll(selector)
            return document.getElementsByClassName(selector.substring(1))
    &#125;else&#123;
        return document['querySelectorAll' ? 'querySelectorAll':'getElementsByTagName'](selector)
    &#125;
&#125; 

/*检测类名*/
hasClass (ele, name) &#123;
    return ele.className.match(new RegExp('(\\s|^)' + name + '(\\s|$)'));
&#125;

/*添加类名*/
addClass (ele, name) &#123;
    if (!this.hasClass(ele, name)) ele.className += " " + name;
&#125;

/*删除类名*/
removeClass (ele, name) &#123;
    if (this.hasClass(ele, name)) &#123;
        var reg = new RegExp('(\\s|^)' + name + '(\\s|$)');
        ele.className = ele.className.replace(reg, '');
    &#125;
&#125;

/*替换类名*/
replaceClass (ele, newName, oldName) &#123;
    this.removeClass(ele, oldName);
    this.addClass(ele, newName);
&#125;

/*获取兄弟节点*/
siblings (ele) &#123;
    console.log(ele.parentNode)
    var chid = ele.parentNode.children,eleMatch = []; 
    for(var i = 0, len = chid.length; i < len; i ++)&#123; 
        if(chid[i] != ele)&#123; 
            eleMatch.push(chid[i]); 
        &#125; 
    &#125; 
    return eleMatch;
&#125;

/*获取行间样式属性*/
getByStyle (obj,name)&#123;
    if(obj.currentStyle)&#123;
        return  obj.currentStyle[name];
    &#125;else&#123;
        return  getComputedStyle(obj,false)[name];
    &#125;
&#125;</pre>
<h3>8. Storage 储存操作</h3>
<pre class="brush: javascript; gutter: true; first-line: 1">class StorageFn &#123;
    constructor () &#123;
        this.ls = window.localStorage;
        this.ss = window.sessionStorage;
    &#125;

    /*-----------------cookie---------------------*/
    /*设置cookie*/
    setCookie (name, value, day) &#123;
        var setting = arguments[0];
        if (Object.prototype.toString.call(setting).slice(8, -1) === 'Object')&#123;
            for (var i in setting) &#123;
                var oDate = new Date();
                oDate.setDate(oDate.getDate() + day);
                document.cookie = i + '=' + setting[i] + ';expires=' + oDate;
            &#125;
        &#125;else&#123;
            var oDate = new Date();
            oDate.setDate(oDate.getDate() + day);
            document.cookie = name + '=' + value + ';expires=' + oDate;
        &#125;

    &#125;

    /*获取cookie*/
    getCookie (name) &#123;
        var arr = document.cookie.split('; ');
        for (var i = 0; i < arr.length; i++) &#123;
            var arr2 = arr[i].split('=');
            if (arr2[0] == name) &#123;
                return arr2[1];
            &#125;
        &#125;
        return '';
    &#125;

    /*删除cookie*/
    removeCookie (name) &#123;
        this.setCookie(name, 1, -1);
    &#125;

    /*-----------------localStorage---------------------*/
    /*设置localStorage*/
    setLocal(key, val) &#123;
        var setting = arguments[0];
        if (Object.prototype.toString.call(setting).slice(8, -1) === 'Object')&#123;
            for(var i in setting)&#123;
                this.ls.setItem(i, JSON.stringify(setting[i]))
            &#125;
        &#125;else&#123;
            this.ls.setItem(key, JSON.stringify(val))
        &#125;

    &#125;

    /*获取localStorage*/
    getLocal(key) &#123;
        if (key) return JSON.parse(this.ls.getItem(key))
        return null;

    &#125;

    /*移除localStorage*/
    removeLocal(key) &#123;
        this.ls.removeItem(key)
    &#125;

    /*移除所有localStorage*/
    clearLocal() &#123;
        this.ls.clear()
    &#125;

    /*-----------------sessionStorage---------------------*/
    /*设置sessionStorage*/
    setSession(key, val) &#123;
        var setting = arguments[0];
        if (Object.prototype.toString.call(setting).slice(8, -1) === 'Object')&#123;
            for(var i in setting)&#123;
                this.ss.setItem(i, JSON.stringify(setting[i]))
            &#125;
        &#125;else&#123;
            this.ss.setItem(key, JSON.stringify(val))
        &#125;

    &#125;

    /*获取sessionStorage*/
    getSession(key) &#123;
        if (key) return JSON.parse(this.ss.getItem(key))
        return null;

    &#125;

    /*移除sessionStorage*/
    removeSession(key) &#123;
        this.ss.removeItem(key)
    &#125;

    /*移除所有sessionStorage*/
    clearSession() &#123;
        this.ss.clear()
    &#125;

&#125;</pre>
<h3>9. Other 其它操作</h3>
<pre class="brush: javascript; gutter: true; first-line: 1">/*获取网址参数*/
getURL(name)&#123;
    var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
    var r = decodeURI(window.location.search).substr(1).match(reg);
    if(r!=null) return  r[2]; return null;
&#125;

/*获取全部url参数,并转换成json对象*/
getUrlAllParams (url) &#123;
    var url = url ? url : window.location.href;
    var _pa = url.substring(url.indexOf('?') + 1),
        _arrS = _pa.split('&'),
        _rs = &#123;&#125;;
    for (var i = 0, _len = _arrS.length; i < _len; i++) &#123;
        var pos = _arrS[i].indexOf('=');
        if (pos == -1) &#123;
            continue;
        &#125;
        var name = _arrS[i].substring(0, pos),
            value = window.decodeURIComponent(_arrS[i].substring(pos + 1));
        _rs[name] = value;
    &#125;
    return _rs;
&#125;

/*删除url指定参数，返回url*/
delParamsUrl(url, name)&#123;
    var baseUrl = url.split('?')[0] + '?';
    var query = url.split('?')[1];
    if (query.indexOf(name)>-1) &#123;
        var obj = &#123;&#125;
        var arr = query.split("&");
        for (var i = 0; i < arr.length; i++) &#123;
            arr[i] = arr[i].split("=");
            obj[arr[i][0]] = arr[i][1];
        &#125;;
        delete obj[name];
        var url = baseUrl + JSON.stringify(obj).replace(/[\"\&#123;\&#125;]/g,"").replace(/\:/g,"=").replace(/\,/g,"&");
        return url
    &#125;else&#123;
        return url;
    &#125;
&#125;

/*获取十六进制随机颜色*/
getRandomColor () &#123;
    return '#' + (function(h) &#123;
        return new Array(7 - h.length).join("0") + h;
    &#125;)((Math.random() * 0x1000000 << 0).toString(16));
&#125;

/*图片加载*/
imgLoadAll(arr,callback)&#123;
    var arrImg = []; 
    for (var i = 0; i < arr.length; i++) &#123;
        var img = new Image();
        img.src = arr[i];
        img.onload = function()&#123;
            arrImg.push(this);
            if (arrImg.length == arr.length) &#123;
                callback && callback();
            &#125;
        &#125;
    &#125;
&#125;

/*音频加载*/
loadAudio(src, callback) &#123;
    var audio = new Audio(src);
    audio.onloadedmetadata = callback;
    audio.src = src;
&#125;

/*DOM转字符串*/
domToStirng(htmlDOM)&#123;
    var div= document.createElement("div");
    div.appendChild(htmlDOM);
    return div.innerHTML
&#125;

/*字符串转DOM*/
stringToDom(htmlString)&#123;
    var div= document.createElement("div");
    div.innerHTML=htmlString;
    return div.children[0];
&#125;

/**
 * 光标所在位置插入字符，并设置光标位置
 * 
 * @param &#123;dom&#125; 输入框
 * @param &#123;val&#125; 插入的值
 * @param &#123;posLen&#125; 光标位置处在 插入的值的哪个位置
 */
setCursorPosition (dom,val,posLen) &#123;
    var cursorPosition = 0;
    if(dom.selectionStart)&#123;
        cursorPosition = dom.selectionStart;
    &#125;
    this.insertAtCursor(dom,val);
    dom.focus();
    console.log(posLen)
    dom.setSelectionRange(dom.value.length,cursorPosition + (posLen || val.length));
&#125;

/*光标所在位置插入字符*/
insertAtCursor(dom, val) &#123;
    if (document.selection)&#123;
        dom.focus();
        sel = document.selection.createRange();
        sel.text = val;
        sel.select();
    &#125;else if (dom.selectionStart || dom.selectionStart == '0')&#123;
        let startPos = dom.selectionStart;
        let endPos = dom.selectionEnd;
        let restoreTop = dom.scrollTop;
        dom.value = dom.value.substring(0, startPos) + val + dom.value.substring(endPos, dom.value.length);
        if (restoreTop > 0)&#123;
            dom.scrollTop = restoreTop;
        &#125;
        dom.focus();
        dom.selectionStart = startPos + val.length;
        dom.selectionEnd = startPos + val.length;
    &#125; else &#123;
        dom.value += val;
        dom.focus();
    &#125;
&#125;</pre>
<h2 id="articleHeader1">CSS</h2>
<h3>1. pc-reset PC样式初始化</h3>
<pre class="brush: css; gutter: true; first-line: 1">/* normalize.css */

html &#123;
  line-height: 1.15;
  /* 1 */
  -ms-text-size-adjust: 100%;
  /* 2 */
  -webkit-text-size-adjust: 100%;
  /* 2 */
&#125;

body &#123;
  margin: 0;
&#125;

article,
aside,
footer,
header,
nav,
section &#123;
  display: block;
&#125;

h1 &#123;
  font-size: 2em;
  margin: 0.67em 0;
&#125;

figcaption,
figure,
main &#123;
  /* 1 */
  display: block;
&#125;

figure &#123;
  margin: 1em 40px;
&#125;

hr &#123;
  box-sizing: content-box;
  /* 1 */
  height: 0;
  /* 1 */
  overflow: visible;
  /* 2 */
&#125;

pre &#123;
  font-family: monospace, monospace;
  /* 1 */
  font-size: 1em;
  /* 2 */
&#125;

a &#123;
  background-color: transparent;
  /* 1 */
  -webkit-text-decoration-skip: objects;
  /* 2 */
&#125;

abbr[title] &#123;
  border-bottom: none;
  /* 1 */
  text-decoration: underline;
  /* 2 */
  text-decoration: underline dotted;
  /* 2 */
&#125;

b,
strong &#123;
  font-weight: inherit;
&#125;

b,
strong &#123;
  font-weight: bolder;
&#125;

code,
kbd,
samp &#123;
  font-family: monospace, monospace;
  /* 1 */
  font-size: 1em;
  /* 2 */
&#125;

dfn &#123;
  font-style: italic;
&#125;

mark &#123;
  background-color: #ff0;
  color: #000;
&#125;

small &#123;
  font-size: 80%;
&#125;

sub,
sup &#123;
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
&#125;

sub &#123;
  bottom: -0.25em;
&#125;

sup &#123;
  top: -0.5em;
&#125;

audio,
video &#123;
  display: inline-block;
&#125;

audio:not([controls]) &#123;
  display: none;
  height: 0;
&#125;

img &#123;
  border-style: none;
&#125;

svg:not(:root) &#123;
  overflow: hidden;
&#125;

button,
input,
optgroup,
select,
textarea &#123;
  font-family: sans-serif;
  /* 1 */
  font-size: 100%;
  /* 1 */
  line-height: 1.15;
  /* 1 */
  margin: 0;
  /* 2 */
&#125;

button,
input &#123;
  /* 1 */
  overflow: visible;
&#125;

button,
select &#123;
  /* 1 */
  text-transform: none;
&#125;

button,
html [type="button"],

/* 1 */

[type="reset"],
[type="submit"] &#123;
  -webkit-appearance: button;
  /* 2 */
&#125;

button::-moz-focus-inner,
[type="button"]::-moz-focus-inner,
[type="reset"]::-moz-focus-inner,
[type="submit"]::-moz-focus-inner &#123;
  border-style: none;
  padding: 0;
&#125;

button:-moz-focusring,
[type="button"]:-moz-focusring,
[type="reset"]:-moz-focusring,
[type="submit"]:-moz-focusring &#123;
  outline: 1px dotted ButtonText;
&#125;

fieldset &#123;
  padding: 0.35em 0.75em 0.625em;
&#125;

legend &#123;
  box-sizing: border-box;
  /* 1 */
  color: inherit;
  /* 2 */
  display: table;
  /* 1 */
  max-width: 100%;
  /* 1 */
  padding: 0;
  /* 3 */
  white-space: normal;
  /* 1 */
&#125;

progress &#123;
  display: inline-block;
  /* 1 */
  vertical-align: baseline;
  /* 2 */
&#125;

textarea &#123;
  overflow: auto;
&#125;

[type="checkbox"],
[type="radio"] &#123;
  box-sizing: border-box;
  /* 1 */
  padding: 0;
  /* 2 */
&#125;

[type="number"]::-webkit-inner-spin-button,
[type="number"]::-webkit-outer-spin-button &#123;
  height: auto;
&#125;

[type="search"] &#123;
  -webkit-appearance: textfield;
  /* 1 */
  outline-offset: -2px;
  /* 2 */
&#125;

[type="search"]::-webkit-search-cancel-button,
[type="search"]::-webkit-search-decoration &#123;
  -webkit-appearance: none;
&#125;

 ::-webkit-file-upload-button &#123;
  -webkit-appearance: button;
  /* 1 */
  font: inherit;
  /* 2 */
&#125;

details,

/* 1 */

menu &#123;
  display: block;
&#125;

summary &#123;
  display: list-item;
&#125;

canvas &#123;
  display: inline-block;
&#125;

template &#123;
  display: none;
&#125;

[hidden] &#123;
  display: none;
&#125;

/* reset */

html,
body,
h1,
h2,
h3,
h4,
h5,
h6,
div,
dl,
dt,
dd,
ul,
ol,
li,
p,
blockquote,
pre,
hr,
figure,
table,
caption,
th,
td,
form,
fieldset,
legend,
input,
button,
textarea,
menu &#123;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
&#125;</pre>
<h3>2. Phone-reset</h3>
<pre class="brush: css; gutter: true; first-line: 1">/* normalize.css */

html &#123;
  line-height: 1.15;
  /* 1 */
  -ms-text-size-adjust: 100%;
  /* 2 */
  -webkit-text-size-adjust: 100%;
  /* 2 */
&#125;

body &#123;
  margin: 0;
&#125;

article,
aside,
footer,
header,
nav,
section &#123;
  display: block;
&#125;

h1 &#123;
  font-size: 2em;
  margin: 0.67em 0;
&#125;

figcaption,
figure,
main &#123;
  /* 1 */
  display: block;
&#125;

figure &#123;
  margin: 1em 40px;
&#125;

hr &#123;
  box-sizing: content-box;
  /* 1 */
  height: 0;
  /* 1 */
  overflow: visible;
  /* 2 */
&#125;

pre &#123;
  font-family: monospace, monospace;
  /* 1 */
  font-size: 1em;
  /* 2 */
&#125;

a &#123;
  background-color: transparent;
  /* 1 */
  -webkit-text-decoration-skip: objects;
  /* 2 */
&#125;

abbr[title] &#123;
  border-bottom: none;
  /* 1 */
  text-decoration: underline;
  /* 2 */
  text-decoration: underline dotted;
  /* 2 */
&#125;

b,
strong &#123;
  font-weight: inherit;
&#125;

b,
strong &#123;
  font-weight: bolder;
&#125;

code,
kbd,
samp &#123;
  font-family: monospace, monospace;
  /* 1 */
  font-size: 1em;
  /* 2 */
&#125;

dfn &#123;
  font-style: italic;
&#125;

mark &#123;
  background-color: #ff0;
  color: #000;
&#125;

small &#123;
  font-size: 80%;
&#125;

sub,
sup &#123;
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
&#125;

sub &#123;
  bottom: -0.25em;
&#125;

sup &#123;
  top: -0.5em;
&#125;

audio,
video &#123;
  display: inline-block;
&#125;

audio:not([controls]) &#123;
  display: none;
  height: 0;
&#125;

img &#123;
  border-style: none;
&#125;

svg:not(:root) &#123;
  overflow: hidden;
&#125;

button,
input,
optgroup,
select,
textarea &#123;
  font-family: sans-serif;
  /* 1 */
  font-size: 100%;
  /* 1 */
  line-height: 1.15;
  /* 1 */
  margin: 0;
  /* 2 */
&#125;

button,
input &#123;
  /* 1 */
  overflow: visible;
&#125;

button,
select &#123;
  /* 1 */
  text-transform: none;
&#125;

button,
html [type="button"],

/* 1 */

[type="reset"],
[type="submit"] &#123;
  -webkit-appearance: button;
  /* 2 */
&#125;

button::-moz-focus-inner,
[type="button"]::-moz-focus-inner,
[type="reset"]::-moz-focus-inner,
[type="submit"]::-moz-focus-inner &#123;
  border-style: none;
  padding: 0;
&#125;

button:-moz-focusring,
[type="button"]:-moz-focusring,
[type="reset"]:-moz-focusring,
[type="submit"]:-moz-focusring &#123;
  outline: 1px dotted ButtonText;
&#125;

fieldset &#123;
  padding: 0.35em 0.75em 0.625em;
&#125;

legend &#123;
  box-sizing: border-box;
  /* 1 */
  color: inherit;
  /* 2 */
  display: table;
  /* 1 */
  max-width: 100%;
  /* 1 */
  padding: 0;
  /* 3 */
  white-space: normal;
  /* 1 */
&#125;

progress &#123;
  display: inline-block;
  /* 1 */
  vertical-align: baseline;
  /* 2 */
&#125;

textarea &#123;
  overflow: auto;
&#125;

[type="checkbox"],
[type="radio"] &#123;
  box-sizing: border-box;
  /* 1 */
  padding: 0;
  /* 2 */
&#125;

[type="number"]::-webkit-inner-spin-button,
[type="number"]::-webkit-outer-spin-button &#123;
  height: auto;
&#125;

[type="search"] &#123;
  -webkit-appearance: textfield;
  /* 1 */
  outline-offset: -2px;
  /* 2 */
&#125;

[type="search"]::-webkit-search-cancel-button,
[type="search"]::-webkit-search-decoration &#123;
  -webkit-appearance: none;
&#125;

 ::-webkit-file-upload-button &#123;
  -webkit-appearance: button;
  /* 1 */
  font: inherit;
  /* 2 */
&#125;

details,

/* 1 */

menu &#123;
  display: block;
&#125;

summary &#123;
  display: list-item;
&#125;

canvas &#123;
  display: inline-block;
&#125;

template &#123;
  display: none;
&#125;

[hidden] &#123;
  display: none;
&#125;

/* reset */

html,
body,
h1,
h2,
h3,
h4,
h5,
h6,
div,
dl,
dt,
dd,
ul,
ol,
li,
p,
blockquote,
pre,
hr,
figure,
table,
caption,
th,
td,
form,
fieldset,
legend,
input,
button,
textarea,
menu &#123;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
&#125;

html,
body &#123;
  /* 禁止选中文本 */
  -webkit-user-select: none;
  user-select: none;
  font: Oswald, 'Open Sans', Helvetica, Arial, sans-serif
&#125;

/* 禁止长按链接与图片弹出菜单 */

a,
img &#123;
  -webkit-touch-callout: none;
&#125;

/*ios android去除自带阴影的样式*/

a,
input &#123;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
&#125;

input[type="text"] &#123;
  -webkit-appearance: none;
&#125;</pre>
<h3>2. Phone-reset</h3>
<pre class="brush: javascript; gutter: true; first-line: 1">/* normalize.css */

html &#123;
  line-height: 1.15;
  /* 1 */
  -ms-text-size-adjust: 100%;
  /* 2 */
  -webkit-text-size-adjust: 100%;
  /* 2 */
&#125;

body &#123;
  margin: 0;
&#125;

article,
aside,
footer,
header,
nav,
section &#123;
  display: block;
&#125;

h1 &#123;
  font-size: 2em;
  margin: 0.67em 0;
&#125;

figcaption,
figure,
main &#123;
  /* 1 */
  display: block;
&#125;

figure &#123;
  margin: 1em 40px;
&#125;

hr &#123;
  box-sizing: content-box;
  /* 1 */
  height: 0;
  /* 1 */
  overflow: visible;
  /* 2 */
&#125;

pre &#123;
  font-family: monospace, monospace;
  /* 1 */
  font-size: 1em;
  /* 2 */
&#125;

a &#123;
  background-color: transparent;
  /* 1 */
  -webkit-text-decoration-skip: objects;
  /* 2 */
&#125;

abbr[title] &#123;
  border-bottom: none;
  /* 1 */
  text-decoration: underline;
  /* 2 */
  text-decoration: underline dotted;
  /* 2 */
&#125;

b,
strong &#123;
  font-weight: inherit;
&#125;

b,
strong &#123;
  font-weight: bolder;
&#125;

code,
kbd,
samp &#123;
  font-family: monospace, monospace;
  /* 1 */
  font-size: 1em;
  /* 2 */
&#125;

dfn &#123;
  font-style: italic;
&#125;

mark &#123;
  background-color: #ff0;
  color: #000;
&#125;

small &#123;
  font-size: 80%;
&#125;

sub,
sup &#123;
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
&#125;

sub &#123;
  bottom: -0.25em;
&#125;

sup &#123;
  top: -0.5em;
&#125;

audio,
video &#123;
  display: inline-block;
&#125;

audio:not([controls]) &#123;
  display: none;
  height: 0;
&#125;

img &#123;
  border-style: none;
&#125;

svg:not(:root) &#123;
  overflow: hidden;
&#125;

button,
input,
optgroup,
select,
textarea &#123;
  font-family: sans-serif;
  /* 1 */
  font-size: 100%;
  /* 1 */
  line-height: 1.15;
  /* 1 */
  margin: 0;
  /* 2 */
&#125;

button,
input &#123;
  /* 1 */
  overflow: visible;
&#125;

button,
select &#123;
  /* 1 */
  text-transform: none;
&#125;

button,
html [type="button"],

/* 1 */

[type="reset"],
[type="submit"] &#123;
  -webkit-appearance: button;
  /* 2 */
&#125;

button::-moz-focus-inner,
[type="button"]::-moz-focus-inner,
[type="reset"]::-moz-focus-inner,
[type="submit"]::-moz-focus-inner &#123;
  border-style: none;
  padding: 0;
&#125;

button:-moz-focusring,
[type="button"]:-moz-focusring,
[type="reset"]:-moz-focusring,
[type="submit"]:-moz-focusring &#123;
  outline: 1px dotted ButtonText;
&#125;

fieldset &#123;
  padding: 0.35em 0.75em 0.625em;
&#125;

legend &#123;
  box-sizing: border-box;
  /* 1 */
  color: inherit;
  /* 2 */
  display: table;
  /* 1 */
  max-width: 100%;
  /* 1 */
  padding: 0;
  /* 3 */
  white-space: normal;
  /* 1 */
&#125;

progress &#123;
  display: inline-block;
  /* 1 */
  vertical-align: baseline;
  /* 2 */
&#125;

textarea &#123;
  overflow: auto;
&#125;

[type="checkbox"],
[type="radio"] &#123;
  box-sizing: border-box;
  /* 1 */
  padding: 0;
  /* 2 */
&#125;

[type="number"]::-webkit-inner-spin-button,
[type="number"]::-webkit-outer-spin-button &#123;
  height: auto;
&#125;

[type="search"] &#123;
  -webkit-appearance: textfield;
  /* 1 */
  outline-offset: -2px;
  /* 2 */
&#125;

[type="search"]::-webkit-search-cancel-button,
[type="search"]::-webkit-search-decoration &#123;
  -webkit-appearance: none;
&#125;

 ::-webkit-file-upload-button &#123;
  -webkit-appearance: button;
  /* 1 */
  font: inherit;
  /* 2 */
&#125;

details,

/* 1 */

menu &#123;
  display: block;
&#125;

summary &#123;
  display: list-item;
&#125;

canvas &#123;
  display: inline-block;
&#125;

template &#123;
  display: none;
&#125;

[hidden] &#123;
  display: none;
&#125;

/* reset */

html,
body,
h1,
h2,
h3,
h4,
h5,
h6,
div,
dl,
dt,
dd,
ul,
ol,
li,
p,
blockquote,
pre,
hr,
figure,
table,
caption,
th,
td,
form,
fieldset,
legend,
input,
button,
textarea,
menu &#123;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
&#125;

html,
body &#123;
  /* 禁止选中文本 */
  -webkit-user-select: none;
  user-select: none;
  font: Oswald, 'Open Sans', Helvetica, Arial, sans-serif
&#125;

/* 禁止长按链接与图片弹出菜单 */

a,
img &#123;
  -webkit-touch-callout: none;
&#125;

/*ios android去除自带阴影的样式*/

a,
input &#123;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
&#125;

input[type="text"] &#123;
  -webkit-appearance: none;
&#125;</pre>
<h3>3. 公共样式提取</h3>
<pre class="brush: javascript; gutter: true; first-line: 1">/* 禁止选中文本 */
.usn&#123;
    -webkit-user-select:none;
    -moz-user-select:none;
    -ms-user-select:none;
    -o-user-select:none;
    user-select:none;
&#125;
/* 浮动 */
.fl &#123; float: left; &#125;
.fr &#123; float: right; &#125;
.cf &#123; zoom: 1; &#125;
.cf:after &#123;
    content:".";
    display:block;
    clear:both;
    visibility:hidden;
    height:0;
    overflow:hidden;
&#125;

/* 元素类型 */
.db &#123; display: block; &#125;
.dn &#123; display: none; &#125;
.di &#123; display: inline &#125;
.dib &#123;display: inline-block;&#125;
.transparent &#123; opacity: 0 &#125;

/*文字排版、颜色*/
.f12 &#123; font-size:12px &#125;
.f14 &#123; font-size:14px &#125;
.f16 &#123; font-size:16px &#125;
.f18 &#123; font-size:18px &#125;
.f20 &#123; font-size:20px &#125;
.fb &#123; font-weight:bold &#125;
.fn &#123; font-weight:normal &#125;
.t2 &#123; text-indent:2em &#125;
.red,a.red &#123; color:#cc0031 &#125;
.darkblue,a.darkblue &#123; color:#039 &#125;
.gray,a.gray &#123; color:#878787 &#125;
.lh150 &#123; line-height:150% &#125;
.lh180 &#123; line-height:180% &#125;
.lh200 &#123; line-height:200% &#125;
.unl &#123; text-decoration:underline; &#125;
.no_unl &#123; text-decoration:none; &#125;
.tl &#123; text-align: left; &#125;
.tc &#123; text-align: center; &#125;
.tr &#123; text-align: right; &#125;
.tj &#123; text-align: justify; text-justify: inter-ideograph; &#125;
.wn &#123; /* 强制不换行 */
    word-wrap:normal;
    white-space:nowrap;
&#125;
.wb &#123; /* 强制换行 */
    white-space:normal;
    word-wrap:break-word;
    word-break:break-all;
&#125;
.wp &#123; /* 保持空白序列*/
    overflow:hidden;text-align:left;white-space:pre-wrap;word-wrap:break-word;word-break:break-all;
&#125;
.wes &#123; /* 多出部分用省略号表示 , 用于一行 */
    overflow:hidden;
    word-wrap:normal;
    white-space:nowrap;
    text-overflow:ellipsis;
&#125;
.wes-2 &#123; /* 适用于webkit内核和移动端 */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
    overflow: hidden;
&#125; 
.wes-3 &#123;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
    overflow: hidden;
&#125;
.wes-4 &#123;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 4;
    overflow: hidden;
&#125;

/* 溢出样式 */
.ofh &#123; overflow: hidden; &#125;
.ofs &#123;overflow: scroll; &#125;
.ofa &#123;overflow: auto; &#125;
.ofv &#123;overflow: visible; &#125;

/* 定位方式 */
.ps &#123;position: static; &#125;
.pr &#123;position: relative;zoom:1; &#125;
.pa &#123;position: absolute; &#125;
.pf &#123;position: fixed; &#125;

/* 垂直对齐方式 */
.vt &#123;vertical-align: top; &#125;
.vm &#123;vertical-align: middle; &#125;
.vb &#123;vertical-align: bottom; &#125;

/* 鼠标样式 */
.csd &#123;cursor: default; &#125;
.csp &#123;cursor: pointer; &#125;
.csh &#123;cursor: help; &#125;
.csm &#123;cursor: move; &#125;

/* flex布局 */
.df-sb &#123;
    display:flex;
    align-items: center;
    justify-content: space-between;
&#125;
.df-sa &#123;
    display:flex;
    align-items: center;
    justify-content: space-around;
&#125;

/* 垂直居中 */
.df-c &#123;
    display: flex;
    align-items: center;
    justify-content: center;
&#125;
.tb-c &#123;
    text-align:center;
    display:table-cell;
    vertical-align:middle;
&#125;
.ts-c &#123;
    position: absolute;
    left: 50%; top: 50%;
    transform: translate(-50%, -50%);
&#125;
.ts-mc &#123;
    position: absolute;
    left: 0;right: 0;
    bottom: 0; top: 0;
    margin: auto;
&#125;

/* 辅助 */
.mask-fixed-wrapper &#123;
    width: 100%;
    height: 100%;
    position: fixed;
    left:0;top:0;
    background: rgba(0, 0, 0, 0.65);
    z-index: 999;
&#125;
.bg-cover &#123;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center center;
&#125;
.bg-cover-all &#123;
    background-size: 100% 100%;
    background-repeat: no-repeat;
    background-position: center center;
&#125;</pre>


<a id="soft-link" name="soft-link" href="http://www.codeceo.com/article/undefined"></a>




<!--开源软件资源链接-->
<!--开源软件资源链接结束-->







  
</div>
            