
---
title: '解析Swagger2.0的接口'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4962'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 02:35:26 GMT
thumbnail: 'https://picsum.photos/400/300?random=4962'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">背景</h1>
<p>项目上会把一个后端接口映射为如下结构</p>
<pre><code class="copyable">  &#123;
    desc: "获取英雄详情",
    method: "post",
    name: "getHeroInfo",
    url: "/api/getHeroInfo",
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果一次新增了10个接口，那么就需要，Ctrl+c、Ctrl+v、切屏...</p>
<h1 data-id="heading-1">方案</h1>
<p>一开始想用无头浏览器来着，看了一下文档请求完全不需要
发起请求: <a href="http://10.200.0.3:59080/swagger-resources" target="_blank" rel="nofollow noopener noreferrer">http://10.200.0.3:59080/swagger-resources</a>
获取有哪些组</p>
<pre><code class="copyable">    [
      &#123;
        name: "background-admin",
        url: "/v2/api-docs?group=background-admin",
        swaggerVersion: "2.0",
        location: "/v2/api-docs?group=background-admin",
      &#125;,
    ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>发起请求  <a href="http://10.200.0.3:59080/v2/api-docs?group=doctor-PC" target="_blank" rel="nofollow noopener noreferrer">http://10.200.0.3:59080/v2/api-docs?group=doctor-PC</a> ，获取组下面有哪些接口，可以说页面上的所有内容都是通过接口生成的，简易结构如下</p>
<pre><code class="copyable">&#123;
      basePath: "/",
      definitions: &#123;
        "ResultVO«英雄详细信息»": &#123;
          type: "object",
          properties: &#123;
            data: &#123;
              description:
                "响应数据：成功时返回需要的数据，失败时返回详细原因或为null",
              $ref: "#/definitions/英雄详细信息",
            &#125;,
            message: &#123;
              type: "string",
              description: "请求状态描述",
            &#125;,
            status: &#123;
              type: "integer",
              format: "int32",
              description: "请求状态码，200-正确，其它-错误",
            &#125;,
          &#125;,
          title: "ResultVO«web医生服务消息配置»",
        &#125;,
        英雄详细信息: &#123;
          type: "object",
          properties: &#123;
            name: &#123;
              type: "string",
              description: "英雄姓名",
            &#125;,
            age: &#123;
              format: "int32",
              type: "integer",
              description: "英雄年龄",
            &#125;,
            birthday: &#123;
              type: "string",
              format: "date-time",
              description: "英雄出生时间",
            &#125;,
            live: &#123;
              type: "boolean",
              description: "现在是否还活着",
            &#125;,
          &#125;,
        &#125;,
      &#125;,
      paths: &#123;
        "/api/getHeroInfo": &#123;
          post: &#123;
            tags: ["英雄信息查询接口"],
            summary: "英雄生平",
            parameters: [
              &#123;
                name: "id",
                in: "query",
                required: true,
                type: "string",
              &#125;,
            ],
            responses: &#123;
              200: &#123;
                description: "OK",
                $ref: "#/definitions/ResultVO«英雄详细信息»",
              &#125;,
              20107: &#123;
                description: "参数异常",
              &#125;,
            &#125;,
            deprecated: false,
          &#125;,
        &#125;,
      &#125;,
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">自动映射</h1>
<p>根据<code>summary </code>属性去匹配，就可以一次性映射该类目下的所有接口</p>
<h1 data-id="heading-3">自动生成mock数据</h1>
<p>先获取所有的组，依次遍历组下面所有的接口
<strong>$ref: "#/definitions/ResultVO«英雄详细信息»",</strong> 所有的结构体都定义在<code>definitions</code>，是互相嵌套的，需要递归去组装结构体</p>
<p>每个参数都有对应的描述</p>
<pre><code class="copyable">            birthday: &#123;
              type: "string",
              format: "date-time",
              description: "英雄出生时间",
            &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以借助 <a href="https://github.com/nuysoft/Mock/wiki/Mock.Random" target="_blank" rel="nofollow noopener noreferrer">Mock.Random</a>，结合具体的项目，生成比Swagger文档上更直观的"响应示例"，比如<code>status</code>的值为200，具体应用可参考 <a href="https://github.com/xiaodun/sf-mock" target="_blank" rel="nofollow noopener noreferrer">github.com/xiaodun/sf-…</a></p></div>  
</div>
            