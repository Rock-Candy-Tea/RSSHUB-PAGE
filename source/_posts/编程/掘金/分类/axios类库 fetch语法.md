
---
title: 'axios类库 fetch语法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=564'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 04:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=564'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">axios是基于promise封装的AJAX类库</h1>
<pre><code class="copyable">        config基本配置
        data 后台拿到的数据
        headers 响应头信息
        request 原生xhr实例
        status/statusText HTTP状态/状态描述
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"> <script src="./node_modules/axios/dist/axios.min.js"></script>
        // axios是基于promise封装的AJAX类库
        axios.get('./1.json').then(res=>&#123;
            console.log(res);
        &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">剖析axios</h2>
<ul>
<li>
<p>baseURL:统一配置基本地址</p>
<ul>
<li>axios.defaults.baseURL = '<a href="http://liuqi.cn1.utools.club/" target="_blank" rel="nofollow noopener noreferrer">liuqi.cn1.utools.club</a>';</li>
</ul>
</li>
<li>
<p>统一配置请求头</p>
<ul>
<li>headers.post给post请求增加请求头</li>
<li>axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';</li>
</ul>
</li>
<li>
<p>给headers.common给所有请求都增加请求头</p>
<ul>
<li>axios.defaults.headers.common['Content-Type'] = 'application/x-www-form-urlencoded';</li>
</ul>
</li>
<li>
<p>transformRequest在post请求之前，调用处理传参，返回值会放在请求体里传给后台</p>
</li>
<li>
<p><code>transformRequest</code> 允许在向服务器发送前，修改请求数据</p>
</li>
<li>
<p>只能用在 'PUT', 'POST' 和 'PATCH' 这几个请求方法</p>
<ul>
<li>axios.defaults.transformRequest = function (data, headers) &#123;
console.log(data, headers);</li>
</ul>
</li>
<li>
<p>统一处理参数的地方</p>
<ul>
<li>return JSON.stringify(data);
&#125;;</li>
</ul>
</li>
</ul>
<pre><code class="copyable">// baseURL拼上/user/add的接口
        // axios.post('/user/add', &#123; id: 21, name: 34 &#125;).then(res => &#123; &#125;);
        // baseURL拼上127.0.0.1:8888/user/add的接口
        // axios.post('127.0.0.1:8888/user/add', &#123; id: 21, name: 34 &#125;).then(res => &#123; &#125;);
        // 当地址是以HTTP或HTTPS开头，会用自己的地址，跟baseURL没关系了
        // axios.post('http://127.0.0.1:8888/user/add', &#123; id: 21, name: 34 &#125;).then(res => &#123; &#125;);
        axios.post('/user/add', &#123; id: 21, name: 34 &#125;, &#123;
        &#125;).then(res => &#123; &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>添加请求拦截器</li>
</ul>
<pre><code class="copyable">axios.defaults.interceptors.resquest.use(function success(config) &#123;
            // 在发送请求之前做些什么
            console.log(config);
            return config;
        &#125;, function error(error) &#123;
            // 对请求错误做些什么
            console.log(error);
            console.log(error);
            return Promise.reject(error);
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>添加响应拦截器</li>
</ul>
<pre><code class="copyable"> axios.defaults.interceptors.response.use(function onSuccess(response) &#123;
          // 对响应数据做点什么
           console.log(response);
            return response;
        &#125;, function onFail(error) &#123;
            // 对响应错误做点什么
            return Promise.reject(error);
        &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">在路径后传递第二个参数，是个对象，对象里面有params对象，参数放在params对象里</h1>
<pre><code class="copyable"> axios.get('./1.json',&#123;params:&#123;id:1&#125;&#125;).then(res=>&#123;&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">post传参：直接第二个参数就是传给后台的</h1>
<pre><code class="copyable">axios.post('./1.json',&#123;id:1&#125;).then(res=>&#123;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">axios手动封装</h2>
<pre><code class="copyable"> // 把my_axios作为普通对象，增加defaults属性，加入一个默认的baseURL
        my_axios.defaults = &#123; baseURL: '' &#125;;
        function my_axios(options) &#123;
            let &#123;
                method = 'get',
                url,
                params,
                data,
                headers
            &#125; = options;
            return new Promise((resolve, reject) => &#123;
                // 统一转大写
                method = method.toUpperCase();
                // 处理地址
                if (url.indexOf('http') !== 0) &#123;
                    url = my_axios.defaults.baseURL + url;
                &#125;;
                // 处理get请求的传参
                if (method === 'GET') &#123;
                    if (url.indexOf('?') > -1) &#123;
                        url += '&' + Qs.stringify(params);
                    &#125; else &#123;
                        url += '?' + Qs.stringify(params);
                    &#125;;
                &#125;;
                let xhr = new XMLHttpRequest;
                xhr.open(method, url);
                // 设置请求头
                Object.keys(headers).forEach(key => &#123;
                    xhr.setRequestHeader(key, headers[key]);
                &#125;);
                xhr.onreadystatechange = function () &#123;
                    if (xhr.readyState === 4 && xhr.status >= 200 && xhr.status < 400) &#123;
                        let test = xhr.responseText;
                        let data = &#123;
                            data: JSON.parse(test),//后台拿到的数据
                            request: xhr,//xhr实例
                            config: '',//axios配置
                            headers: '',//响应头
                            status: xhr.status,//HTTP状态码
                            statusText: xhr.statusText//状态描述
                        &#125;;
                        resolve(data);
                    &#125; else if (xhr.readyState === 4 && xhr.status >= 400) &#123;
                        reject(xhr.response);
                    &#125;;
                &#125;;
                xhr.send(data ? JSON.stringify(data) : null);
            &#125;);
        &#125;;

        // baseURL统一配置基本地址
        my_axios.defaults.baseURL = '';
        my_axios(&#123;
            method: 'get',
            url: './1.json',
            params: &#123; id:1&#125;,
            data:&#123;name:'haha'&#125;,
            headers: &#123;&#125;
        &#125;).then(res => &#123;
            console.log(res);
        &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">fetch</h1>
<pre><code class="copyable">// fetch语法
fetch('./data.json').then(response=>&#123;
    // response中包含了服务器返回的信息；响应主体信息response.body[ReadableStream可读流信息]，我们需要把可读流信息变成指定格式
    // + Response.prototype.json/text/blob/arrayBuffer.....
    // + 执行这些方法中的任何一个，返回的结果都是promise实例：如果可以把响应主体信息正常转换为指定格式，则promise的状态是fulfilled、值是转换为的数据内容，如果不能正常转换，则状态是失败的....
    // + 一旦执行了其中的一个方法，再执行其他方法会出问题
    return response.json()
    // console.log(response);
&#125;).then(value=>&#123;
    console.log(value); //["zhufengpeixun"]
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">fetch和axios的区别：</h2>
<ul>
<li>他俩都是发送数据的</li>
<li>axios是基于promise封装的AJAX的类库</li>
<li>fetch是浏览器原生的API</li>
<li>传参字段不一样，axios是放在params里或者data里，fetch是放在body里</li>
<li>node环境不支持fetch，需要引入node-fetch文件才能支持</li>
<li>axios中的配置和拦截器等功能，fetch中都没有。</li>
</ul></div>  
</div>
            