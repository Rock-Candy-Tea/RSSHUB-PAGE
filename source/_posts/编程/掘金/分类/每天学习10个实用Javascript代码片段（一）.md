
---
title: '每天学习10个实用Javascript代码片段（一）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/080a9f3764c0463c81dce37a247abd8c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 03:52:56 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/080a9f3764c0463c81dce37a247abd8c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>随着 Javascript 越来越流行，使其应用的场景越来越多，不仅限于前端，可以是后端、混合应用程序、嵌入式设备等等，于是就有了大前端的叫法。现代前端开发有大量的框架和代码库来帮助实现各种复杂的需求，导致让很多人认为前端开发很简单，如切页面、组框架、网页制作等等。一个前端工程师如果需要提升技能，必然要经历原生代码的编写，代码片段可以加深对 Javascript 基础语法的理解，同时还能增加编码水平。</p>
<h3 data-id="heading-0">1. localStorage</h3>
<p><code>localStorage</code> 是HTML5中的本地持久化存储方法之一，也是前端项目常用的本地存储方案之一。<code>localStorage</code> 存储的数据只要用户不去主动清除是永久存储的，存储的值只能是 <code>string</code> 类型，不能跨浏览器，不能跨域名访问，存储大小一般是 <strong>5M</strong> 左右。下面的代码片段是 <code>localStorage</code> 数据的存储、获取、清除。</p>
<pre><code class="copyable">const useStorage = (storageKey = "authorization") => &#123;
    const localKey = `devpoint.local.$&#123;storageKey&#125;`;
    const save = (data) => &#123;
        window.localStorage.setItem(localKey, JSON.stringify(data));
    &#125;;

    const get = () => &#123;
        const localData = window.localStorage.getItem(localKey);
        if (localData && localData !== "") &#123;
            return JSON.parse(localData);
        &#125; else &#123;
            return false;
        &#125;
    &#125;;
    /**
     * 清除localStorage
     */
    const clear = () => &#123;
        window.localStorage.setItem(localKey, "");
    &#125;;
    return &#123;
        save,
        get,
        clear,
    &#125;;
&#125;;
const storageAuth = useStorage();
const loginInfo = &#123;
    username: "hballard",
    age: 30,
&#125;;
storageAuth.save(loginInfo);
console.log(storageAuth.get());
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/080a9f3764c0463c81dce37a247abd8c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
在浏览器中执行后，结果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8075f0a43dd94f68b74f4efaf7fe50d7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">2. average</h3>
<p>此代码片段返回两个或多个数值的平均值，此代码也展示了如何定义可变参数。</p>
<pre><code class="copyable">const average = (...nums) =>
    nums.reduce((acc, val) => acc + val, 0) / nums.length;

const ages = [30, 24, 28, 32];
console.log(average(...ages)); // 28.5
console.log(average(30, 24, 28, 32)); // 28.5
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">3. averageBy</h3>
<p>此代码片段计算map数组按照指定 <code>key</code> 值的平均值，也可以给定一个迭代函数。</p>
<pre><code class="copyable">const averageBy = (array, fn) =>
    array
        .map(typeof fn === "function" ? fn : (val) => val[fn])
        .reduce((acc, val) => acc + val, 0) / array.length;
const users = [
    &#123; name: "hballard", age: 30 &#125;,
    &#123; name: "sguzman", age: 24 &#125;,
    &#123; name: "jrowe", age: 28 &#125;,
    &#123; name: "plowe", age: 32 &#125;,
];
const average1 = averageBy(users, (item) => item.age);
const average2 = averageBy(users, "age");
console.log(average1); // 28.5
console.log(average2); // 28.5
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">4. all</h3>
<p>此代码片段是对集合元素进行验证，如果所有元素通过验证返回 <code>true</code> ，否则返回 <code>false</code>。</p>
<pre><code class="copyable">const all = (array, fn) => array.every(fn);

const ages = [30, 24, 28, 32];
const result1 = all(ages, (item) => item < 40);
const result2 = all(ages, (item) => item > 30);

console.log(result1); // true
console.log(result2); // false
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">5. arrayToCSV</h3>
<p>此代码片段将没有逗号或双引号的元素转换为具有逗号分隔符的字符串，即 <code>csv</code> 文件格式。</p>
<pre><code class="copyable">const arrayToCSV = (array, delimiter = ",") =>
    array
        .map((item) => item.map((value) => `"$&#123;value&#125;"`).join(delimiter))
        .join("\n");

const users = [
    &#123; name: "hballard", age: 30 &#125;,
    &#123; name: "sguzman", age: 24 &#125;,
    &#123; name: "jrowe", age: 28 &#125;,
    &#123; name: "plowe", age: 32 &#125;,
];
const arrayUsers = users.map((item) => Object.values(item));
console.log(arrayUsers);
// [
//     [ 'hballard', 30 ],
//     [ 'sguzman', 24 ],
//     [ 'jrowe', 28 ],
//     [ 'plowe', 32 ]
//   ]
const strCsv1 = arrayToCSV(arrayUsers);
const strCsv2 = arrayToCSV(arrayUsers, ";");

console.log(strCsv1);
// "hballard","30"
// "sguzman","24"
// "jrowe","28"
// "plowe","32"
console.log(strCsv2);
// "hballard";"30"
// "sguzman";"24"
// "jrowe";"28"
// "plowe";"32"
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">6. arrayToHtmlList</h3>
<p>此代码片段将数组元素转换为 <code><li></code> 标记 或者指定html标记，主要用于将数据转换为界面HTML格式。</p>
<pre><code class="copyable">const arrayToHtmlList = (array, tag = "li") =>
    array.map((item) => `<$&#123;tag&#125;>$&#123;item&#125;</$&#123;tag&#125;>`).join("");

console.log(arrayToHtmlList(["第一条", "第二条"])); // <li>第一条</li><li>第二条</li>
console.log(arrayToHtmlList(["第一条", "第二条"], "p")); // <p>第一条</p><p>第二条</p>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">7. allEqual</h3>
<p>此代码片段判断一维数组的所有元素是否全相等。</p>
<pre><code class="copyable">const allEqual = (array) => array.every((val) => val === array[0]);

console.log(allEqual([1, 1, 1, "1"])); // false
console.log(allEqual([1, 1, 1, 2])); // false
console.log(allEqual([1, 1, 1, 1])); // true
console.log(allEqual(["a", "a", "a"])); // true
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">8. countOccurrences</h3>
<p>此代码片段计算数组中某个值的重复次数。</p>
<pre><code class="copyable">const countOccurrences = (array, value) =>
    array.reduce(
        (accumulator, current) =>
            current === value ? accumulator + 1 : accumulator,
        0
    );

console.log(countOccurrences([..."chinese"], "e")); // 2
console.log(countOccurrences([1, 3, 3, 4, 3, 3, 2, 3], 3)); // 5
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">9. capitalizeWord</h3>
<p>此代码片段将给定字符串中每个单词的首字母转为大写。</p>
<pre><code class="copyable">const capitalizeWord = (string) =>
    string.replace(/\b[a-z]/g, (char) => char.toUpperCase());

console.log(capitalizeWord("hello world in javascript")); // Hello World In Javascript
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">10. byteSize</h3>
<p>此代码片段计算给定字符串的字节长度，此代码片段仅限高级浏览器中有效。</p>
<pre><code class="copyable">const byteSize = (string) => new Blob([string]).size;

console.log(byteSize("hello")); // 5
console.log(byteSize("中国")); // 6
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            