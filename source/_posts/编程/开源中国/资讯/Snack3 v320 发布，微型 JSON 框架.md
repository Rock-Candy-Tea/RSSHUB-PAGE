
---
title: 'Snack3 v3.2.0 发布，微型 JSON 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9205'
author: 开源中国
comments: false
date: Tue, 12 Oct 2021 12:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9205'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Snack3 v3.2.0 已经发布，微型 JSON 框架。</p> 
<p>此版本更新内容包括：</p> 
<ul> 
 <li> <p>Constants 更名为 Options，并优化细节</p> </li> 
 <li> <p>ONode::get(key) ，不再自动为文档树添加节点；如有需要改用 ONode::getOrNew(key)</p> </li> 
 <li> <p>增加自定义编码与解码支持</p> </li> 
</ul> 
<pre><code>import org.noear.snack.core.Options;

import java.util.Date;

public class DemoTest &#123;
    public void test(UserDto user) &#123;
        Options options = Options.def();
        options.addEncoder(Date.class, (data, node)->&#123;
            node.val().setNumber(data.getTimes());
        &#125;);
        
        ONode oNode = ONode.loadObj(user, options);
    &#125;
&#125;
</code></pre> 
<p>详情查看：<a href="https://gitee.com/noear/snack3/releases/v3.2.0">https://gitee.com/noear/snack3/releases/v3.2.0</a></p>
                                        </div>
                                      
</div>
            