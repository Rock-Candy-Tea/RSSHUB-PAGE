
---
title: 'JS 实现个位数四则运算'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2431'
author: 掘金
comments: false
date: Sat, 08 May 2021 20:49:18 GMT
thumbnail: 'https://picsum.photos/400/300?random=2431'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>四则运算式，先乘除后加减
数 0～9，+-*/，没有括号</p>
<h4 data-id="heading-0">1. 算法思路</h4>
<p>低优先级操作符遇到其右侧高优先级操作符，右侧优先运算
相同优先级的操作符，左侧优先运算
高优先级操作符遇到其右低优先级操作符，左侧优先运算</p>
<h4 data-id="heading-1">2. 数据结构采用栈结构</h4>
<h4 data-id="heading-2">3. 单元测试</h4>
<pre><code class="copyable">let x = '3+2*3+6/3+6/2+9/3+5*3-8'

// 操作符优先级 0 ～ 1
let OPERATOR = [['+', 0], ['-', 0], ['*', 1], ['/', 1]]

function run (x) &#123;
let nArr = []
let oArr = []

let iRet = ''
let i = 0 // 头指针

let sNToken = x.charCodeAt(i) - 48
let sPToken = ''
let nPriority = 0

if (sNToken < 0 || sNToken > 9) &#123;
iRet = `Error at position $&#123;i&#125; : is not a number($&#123;x.charAt(i)&#125;)!`
&#125; else &#123;
nArr.push(sNToken)
i = 1
for (; i < x.length - 1 ;) &#123;
// 获取操作符
sPToken = x.charAt(i);
// 验证操作符，获取优先级
nPriority = validateOperator(sPToken)
if (typeof nPriority !== 'number') &#123;
iRet = `nPriority at position $&#123;i&#125;`
break 
&#125;

// 获取第二个数
sNToken = x.charCodeAt(i + 1) - 48
if (sNToken < 0 || sNToken > 9) &#123;
iRet = `Error at position $&#123;i + 1&#125; : is not a number($&#123;x.charAt(i + 1)&#125;)!`
&#125;

// 比较 优先级
(typeof(iRet = stackOut(oArr, nArr, false, nPriority)) == 'string') ? true : iRet = '';

if (iRet) &#123;
break
&#125;

// 压栈
nArr.push(sNToken)
let opPair = []
opPair[0] = sPToken
opPair[1] = nPriority

oArr.push(opPair)
i += 2
&#125;

(typeof(iRet = stackOut(oArr, nArr, true)) == 'string')?true:iRet='';
&#125;

if (iRet) &#123;
console.log(iRet)
&#125; else &#123;
nRet = nArr.pop()
&#125;

return nRet
&#125;

function stackOut (oArr, nArr, bIsNotCareAboutPriority, nPriority) &#123;
let iRet = ''
// 操作符栈顶元素的优先级是否大于当前优先级
//let flag = oArr.length != 0 && (bIsNotCareAboutPriority || oArr[oArr.length - 1][1] >= nPriority)
while (oArr.length != 0 && (bIsNotCareAboutPriority || oArr[oArr.length - 1][1] >= nPriority)) &#123;
// 弹栈计算
let n
let n2 = nArr.pop()
let n1 = nArr.pop()
let op = oArr.pop()[0]

n = calculate(op, n1, n2)

if (typeof n !== 'number') &#123;
iRet = n;
&#125; else &#123;
nArr.push(n)
&#125;
&#125;

return iRet === '' ? true : iRet
&#125;

function calculate (op, n1, n2) &#123;
let n;
let iRet = ''
switch (op) &#123;
case '+': n = n1 + n2; break;
case '-': n = n1 - n2; break;
case '*': n = n1 * n2; break;
case '/': n = n1 / n2; break;
default:
iRet = `Error in calculate $&#123;op&#125;`
console.log(iRet)
break
&#125;

if (iRet !== '' && (!isFinite(n) || isNaN(n))) &#123;
iRet = 'Error, the result is invalid'
&#125;

return iRet === '' ? n : iRet
&#125;

function validateOperator (sPToken) &#123;
let iRet = ''
let j = 0
for (j = 0; j < OPERATOR.length; j++) &#123;
if (OPERATOR[j][0] == sPToken) &#123;
break
&#125;
&#125;

if (j >= OPERATOR.length) &#123;
iRet = `Error: Syntax error: invalid operator "$&#123;sPToken&#125;"`
&#125;

return iRet === '' ? OPERATOR[j][1] : iRet
&#125;

console.log(run(x))
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            