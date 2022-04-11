
---
title: 'avue v2.9.5 发布，基于 Element 的前端框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5877'
author: 开源中国
comments: false
date: Mon, 11 Apr 2022 09:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5877'
---

<div>   
<div class="content">
                                                                    
                                                        <p>avue v2.9.5 已经发布，基于 Element 的前端框架。</p> 
<p>此版本更新内容包括：</p> 
<h2>v2.9.5</h2> 
<p><code>2022-04-08</code></p> 
<p><code>调整</code></p> 
<ul> 
 <li>crud组件中的search-change、row-save、row-del、row-update方法里返回表单数据去掉空数据和字典字段，如果要使用字典请使用v-model绑定</li> 
 <li>form组件中的submit方法返回表单数据去掉了空数据和字典字典，如果要使用字典请使用v-model绑定</li> 
 <li>删除了empty组件使用最新的ele的<a href="https://gitee.com/link?target=https%3A%2F%2Felement.eleme.cn%2F%23%2Fzh-CN%2Fcomponent%2Fempty" target="_blank">empty组件</a></li> 
</ul> 
<p><code>新增</code></p> 
<ul> 
 <li>新增crud组件搜索searchFilterDic、searchFilterNull、searchFilterParam三个过滤参数,<a href="https://gitee.com/link?target=https%3A%2F%2Favuejs.com%2Fcrud%2Fcrud-search.html%23%25E6%2590%259C%25E7%25B4%25A2%25E8%25BF%2587%25E6%25BB%25A4" target="_blank">在线例子</a></li> 
 <li>新增crud组件的clearFilter函数<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fnmxiaowei%2Favue%2Fpull%2F550" target="_blank">github_pr_550</a></li> 
</ul> 
<p><code>修复</code></p> 
<ul> 
 <li>修复bind深结构绑定setAsVal函数的数据类型问题<a href="https://gitee.com/smallweigit/avue/issues/I50833" target="_blank">gitee_I50833</a>,<a href="https://gitee.com/link?target=https%3A%2F%2Favuejs.com%2Fform%2Fform-bind" target="_blank">在线例子</a></li> 
 <li>修复inputTable函数的选中和删除问题<a href="https://gitee.com/smallweigit/avue/issues/I50JLF" target="_blank">gitee_I50JLF</a>,<a href="https://gitee.com/link?target=https%3A%2F%2Favuejs.com%2Fform%2Fform-input-table" target="_blank">在线例子</a></li> 
 <li>修复内部一些国际化的问题<a href="https://gitee.com/smallweigit/avue/issues/I4ZEBD" target="_blank">gitee_I4ZEBD</a></li> 
 <li>修复select组件多级联动传参问题<a href="https://gitee.com/smallweigit/avue/issues/I50OED" target="_blank">gitee_I50OED</a></li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/smallweigit/avue/releases/v2.9.5">https://gitee.com/smallweigit/avue/releases/v2.9.5</a></p>
                                        </div>
                                      
</div>
            