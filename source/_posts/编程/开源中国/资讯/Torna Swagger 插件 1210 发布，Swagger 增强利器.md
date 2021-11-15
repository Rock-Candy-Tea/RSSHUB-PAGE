
---
title: 'Torna Swagger 插件 1.2.10 发布，Swagger 增强利器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-8e50d53615ac62eb04f5f5058a37d2211f4.png'
author: 开源中国
comments: false
date: Mon, 15 Nov 2021 08:55:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-8e50d53615ac62eb04f5f5058a37d2211f4.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Torna Swagger 插件 1.2.10 发布，本次更新内容如下：</p> 
<p>- 支持定义错误码 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ftorna.cn%2Fdev%2Fswagger-plugin.html%23%25E6%258E%25A8%25E9%2580%2581%25E9%2594%2599%25E8%25AF%25AF%25E7%25A0%2581" target="_blank">doc</a></p> 
<p>在配置文件中新增codes节点，用来定义错误码或者枚举</p> 
<pre><code class="language-json">// 定义全局错误码，也可以定义枚举
  "codes": [
    // 每一项表示一个分组
    // 定义错误码
    &#123;
      "name": "错误码", // 分组名称
      "description": "这里是全局错误码", // 错误码描述
      "itemType": "string", // 错误码类型
      "items": [
        &#123; "value": "W_10001", "description": "参数错误" &#125;,
        &#123; "value": "W_10002", "description": "缺少token" &#125;,
        &#123; "value": 10000, "type": "number", "description": "缺少参数" &#125; // 单独指定类型
      ]
    &#125;,
    // 定义枚举
    &#123;
      "name": "订单状态枚举",
      "itemType": "number",
      "items": [
        &#123; "name": "WAIT_PAY", "value": 0, "description": "未支付" &#125;,
        &#123; "name": "HAS_PAY", "value": 1, "description": "已支付" &#125;,
        &#123; "name": "CANCEL", "value": 2, "description": "取消支付" &#125;
      ]
    &#125;,
    &#123;
      "name": "用户状态",
      "itemType": "number",
      "items": [
        &#123; "name": "ENABLE", "value": 1, "description": "启用" &#125;,
        &#123; "name": "DISABLE", "value": 0, "description": "禁用" &#125;
      ]
    &#125;
  ]</code></pre> 
<p>推送到Torna后台，将会看到定义后的内容。</p> 
<p><img alt height="270" src="https://oscimg.oschina.net/oscnet/up-8e50d53615ac62eb04f5f5058a37d2211f4.png" width="591" referrerpolicy="no-referrer"></p> 
<p>关于Torna Swagger</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ftorna.cn%2F" target="_blank">Torna</a>配套Swagger插件，可以将代码中申明的swagger注解文档推送到Torna平台，统一进行管理。</p> 
<p>使用Torna Swagger插件的好处有：</p> 
<ul> 
 <li>不用启动项目即可查看文档，调试接口</li> 
 <li>可区分多环境调试（开发环境、测试环境）</li> 
 <li>项目中只需要依赖swagger注解jar即可</li> 
 <li>可定义第三方jar中没有写注解的类</li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            