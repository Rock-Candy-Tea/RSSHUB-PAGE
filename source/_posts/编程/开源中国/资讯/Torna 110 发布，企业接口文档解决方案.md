
---
title: 'Torna 1.1.0 发布，企业接口文档解决方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-3b2d3a461b6d2900f67bfe016de633127bc.png'
author: 开源中国
comments: false
date: Wed, 24 Mar 2021 08:43:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-3b2d3a461b6d2900f67bfe016de633127bc.png'
---

<div>   
<div class="content">
                                                                                            <p>Torna 1.1.0 发布，本次更新内容如下：</p> 
<ul> 
 <li>[feat]支持Mock</li> 
 <li>[fix]文档分类无法删除问题 <a href="https://gitee.com/durcframework/torna/issues/I3CPJ5" target="_blank">#I3CPJ5</a></li> 
 <li>[fix]smart-doc推送无法删除旧文档问题 <a href="https://gitee.com/durcframework/torna/issues/I3CPJL" target="_blank">#I3CPJL</a></li> 
</ul> 
<p>本次更新主要内容是新增了Mock请求，<span style="background-color:#fbfbfb; color:#24292e">在后端没有提供接口数据的情况下，前端开发人员可以配置Mock，模拟返回数据。</span></p> 
<p>开发人员可以编写Mock脚本（基于<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmockjs.com%2F" target="_blank">mockjs</a>）生成数据。</p> 
<p><span style="background-color:#fbfbfb; color:#24292e">例子1</span></p> 
<p><span style="background-color:#fbfbfb; color:#24292e"><img alt height="400" src="https://oscimg.oschina.net/oscnet/up-3b2d3a461b6d2900f67bfe016de633127bc.png" width="572" referrerpolicy="no-referrer"></span></p> 
<p><span style="background-color:#fbfbfb; color:#24292e">可点击</span><code>运行</code><span style="background-color:#fbfbfb; color:#24292e">调试是否可行，没有问题后，点击保存，然后使用postman请求结果如下：</span></p> 
<p><span style="background-color:#fbfbfb; color:#24292e"><img alt height="500" src="https://oscimg.oschina.net/oscnet/up-b843bf420bc083552b913da962bbc83c532.png" width="940" referrerpolicy="no-referrer"></span></p> 
<p>例子2：编写多个函数</p> 
<pre><code class="language-javascript">function getItems() &#123;
    return Mock.mock(&#123;
      "items|4-10": [
        &#123; "id": 2, "label": "手机" &#125;
      ]
    &#125;)
&#125;

function getName() &#123;
    return "分类";
&#125;

var data = &#123;
    "id": 1,
    "name": getName()
&#125;
var items = getItems()
Object.assign(data, items)
// 最后一行返回
return data;</code></pre> 
<p>运行结果：</p> 
<pre><code class="language-json">&#123;
    "id": 1,
    "name": "分类",
    "items": [
        &#123;
            "id": 2,
            "label": "手机"
        &#125;,
        &#123;
            "id": 2,
            "label": "手机"
        &#125;,
        &#123;
            "id": 2,
            "label": "手机"
        &#125;,
        &#123;
            "id": 2,
            "label": "手机"
        &#125;
    ]
&#125;</code></pre> 
<p>例子3：<span style="background-color:#fbfbfb; color:#24292e">扩展</span></p> 
<pre><code class="language-javascript">var random = Mock.Random;

//扩展数据模板
random.extend(&#123;
  type: function(index) &#123;
    const types = ['products', 'industryApp', 'solution', 'experts'];
    return this.pick(types[index])
  &#125;
&#125;);

// 定义数据类型
const menuSource = [];
menuSource[0] = Mock.mock(&#123;
  "type": "@type(0)",
   'data|3-4':[&#123;
     'id|+1': 1,
     name: "@ctitle( 4,6)",
     "childs|5-10": [&#123;
       'id|+1': 1,
       name: "@ctitle(4,6)",
     &#125;]
   &#125;]
&#125;);

return menuSource;</code></pre> 
<p>运行结果：</p> 
<pre><code class="language-json">[
    &#123;
        "type": "products",
        "data": [
            &#123;
                "id": 1,
                "name": "心没积战",
                "childs": [
                    &#123;
                        "id": 1,
                        "name": "决料听国立"
                    &#125;
                ]
            &#125;,
            &#123;
                "id": 2,
                "name": "属化政却外",
                "childs": [
                    &#123;
                        "id": 2,
                        "name": "众他易族"
                    &#125;,
                    &#123;
                        "id": 3,
                        "name": "结值自别难"
                    &#125;
                ]
            &#125;
        ]
    &#125;
]</code></pre> 
<p style="text-align:left">关于<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ftorna.cn" target="_blank">Torna</a></p> 
<p style="text-align:left">企业接口文档解决方案，目标是让文档管理变得更加方便、快捷。Torna采用团队协作的方式管理和维护项目API文档，将不同形式的文档纳入进来，形成一个统一的维护方式。</p> 
<p style="text-align:left"><img height="80%" src="https://gitee.com/durcframework/torna/raw/master/front/public/static/images/arc.png" width="80%" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            