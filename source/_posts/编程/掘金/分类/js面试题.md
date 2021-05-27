
---
title: 'js面试题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8684'
author: 掘金
comments: false
date: Wed, 26 May 2021 23:55:18 GMT
thumbnail: 'https://picsum.photos/400/300?random=8684'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">题目<a href="https://juejin.cn/post/6937892567396646948" target="_blank">juejin.cn/post/693789…</a></h2>
<h2 data-id="heading-1">面试题</h2>
<h3 data-id="heading-2">1.随机打乱</h3>
<pre><code class="hljs language-let copyable" lang="let">        function shuffle(arr) &#123;
          arr.sort(() => Math.random() - 0.5);
          return arr;
        &#125;
        console.log(shuffle(a));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2.反转</h3>
<pre><code class="copyable">        let str = "I am a student!";
        function reserver(str) &#123;
          console.log(str.split("").reverse().join(""));
        &#125;
        reserver(str);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">3.找交集</h3>
<pre><code class="copyable">       function fun(arg) &#123;
        let args = arguments;
        let result = [];
        let flag = false;
        [...args].map((item, index) => &#123;
          minArr = item;
          if (item.length < minArr) &#123;
            minArr = item;
          &#125;
        &#125;);
        minArr.map((item, index) => &#123;
          flag = [...args].every((ite) => ite.includes(item));
          flag && result.push(item);
        &#125;);
        console.log(result);
        return result;
      &#125;
      fun([1, 2, 3], [2, 3, 4], [2, 3], [1, 3, 5]);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">4.手写JSON.stringfy</h3>
<pre><code class="copyable">      const stringOrOtherVal = (data) => &#123;
        if (typeof data === "string") &#123;
          return `"$&#123;data&#125;"`;
        &#125; else &#123;
          return `$&#123;data&#125;`;
        &#125;
      &#125;;

      const myStringfy = (params)=> &#123;
        let resultStr = "&#123;";
        for (let key in params) &#123;
          resultStr += `"$&#123;key&#125;":$&#123;stringOrOtherVal(params[key])&#125;,`;
        &#125;
        resultStr = resultStr.slice(0, resultStr.length - 1);
        resultStr += "&#125;";
        console.log(resultStr);
        return resultStr;
      &#125;;

      let obj1 = &#123; nane: "李明", age: 20 &#125;;
      let obj2 = &#123; name: "李明", age: 20, 12: function () &#123;&#125; &#125;;
      myStringfy([1,2,3,4,8])
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">5.写一个节流函数</h3>
<pre><code class="copyable">     let btn = document.getElementById("btn");
     
      function logs() &#123;
        console.log(1);
      &#125;
      
      btn.addEventListener("click", debounce(logs, 500), false);

      function resize(func, wait) &#123;
        let timeout;
        return function () &#123;
          if (!timeout) &#123;
            timeout = setTimeout(() => &#123;
              timeout = null;
              func.apply(this, arguments);
            &#125;, wait);
          &#125;
        &#125;;
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">6.三次失败走reject</h3>
<pre><code class="copyable">
      let myAxios = function (option) &#123;
        console.log("myAxios");
        return new Promise((resolve, reject) => &#123;
          setTimeout(() => &#123;
            reject("error");
          &#125;, 1000);
        &#125;);
      &#125;;

      function runAxios(option, retry = 2) &#123;
        let p = myAxios(option);
        if (retry > 0) &#123;
          retry--;
          return new Promise((resolve, reject) => &#123;
            p.then(resolve).catch(() => &#123;
              resolve(runAxios(option, retry));
            &#125;);
          &#125;);
        &#125;
        return p;
      &#125;

      runAxios(&#123;
        url: "123/12",
      &#125;)
        .then(() => &#123;
          console.log("success");
        &#125;)
        .catch((err) => &#123;
          console.log("err");
        &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">面试题总结</h3>
<ul>
<li>第1，2，3题还可以，第5题只有在<code>addEventListener</code>中才可以调用，在<code>window.onresize=function()&#123;&#125;</code>,调用失败。第4，6完全不会，也不知道代码对不对。</li>
</ul>
<h2 data-id="heading-9">笔试</h2>
<h3 data-id="heading-10">字符串拼接</h3>
<pre><code class="copyable">      function toString(map) &#123;
        return Object.keys(map)
          .map((item, index) => &#123;
            return (item = `$&#123;item&#125;=$&#123;map[item]&#125;`);
          &#125;)
          .join("&");
      &#125;
      console.log(toString(&#123; a: 1, b: 2, c: 3 &#125;))
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">2.比较字符大小</h3>
<pre><code class="copyable">      function sort(str) &#123;
        return str
          .split("")
          .sort((a, b) => &#123;
            return b.charCodeAt(0) - a.charCodeAt(0);
          &#125;)
          .join("");
      &#125;
      console.log(sort("LeBronJames"));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">3.正则替换</h3>
<pre><code class="copyable">    function camel2snake(str) &#123;
        return str.replace(/[A-Z]/g, (match) => `_$&#123;match.toLowerCase()&#125;`);
      &#125;
      console.log(camel2snake("fateStayNight"));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">4.数组扁平化，递归</h3>
<pre><code class="copyable">    function flattenDeep(list) &#123;
        var flattenArr = [];
        for (var item of list) &#123;
          if (typeof item == "number") &#123;
            flattenArr.push(item);
          &#125; else &#123;
            flattenArr = flattenArr.concat(flattenDeep(item));
          &#125;
        &#125;
        return flattenArr;
      &#125;

      function flattenDeep1(list) &#123;
        return list.flat(Infinity);
      &#125;

      console.log(flattenDeep([1, 2, [2, [3, [4], 5]]]));
      console.log(flattenDeep1([1, [2, [3, [4], 5]]]));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">5.hash使用</h3>
<pre><code class="copyable">     function count(list) &#123;
        const map = new Map();
        for (var str of list) &#123;
          if (map.has(str)) &#123;
            map.set(str, map.get(str)+1);
          &#125; else &#123;
            map.set(str, 1);
          &#125;
        &#125;
        return Object.fromEntries(map);
      &#125;
      console.log(count(["a", "a", "b", "c", "b", "a"]));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">笔试总结</h3>
<ul>
<li>总体相对来说还行，第二题的<code>charCodeAt</code>和第三题 正则也是看了官方api才知道，还得多学多练。</li>
</ul></div>  
</div>
            