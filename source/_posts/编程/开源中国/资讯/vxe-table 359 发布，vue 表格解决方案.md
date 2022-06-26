
---
title: 'vxe-table 3.5.9 发布，vue 表格解决方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7071'
author: 开源中国
comments: false
date: Sat, 25 Jun 2022 23:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7071'
---

<div>   
<div class="content">
                                                                                            <p>vxe-table 3.5.9 已经发布，vue 表格解决方案。</p> 
<p>此版本更新内容包括：</p> 
<ul> 
 <li>table 
  <ul> 
   <li>（v3保留兼容）参数 edit-config.activeMethod 更改为 edit-config.beforeEditMethod</li> 
   <li>（向下兼容）loading图标更改，使用新图标：<code>setup(&#123; icon: &#123; LOADING: 'vxe-icon--refresh roll' &#125; &#125;)</code> <code>setup(&#123; loadingText: '加载中' &#125;)</code>，还原旧图标：<code>setup(&#123; icon: &#123; LOADING: null &#125; &#125;)</code> <code>setup(&#123; loadingText: null &#125;)</code></li> 
   <li>增加参数 scrool-x.scrollToLeftOnChange</li> 
   <li>增加参数 scrool-y.scrollToTopOnChange</li> 
   <li>渲染器增加参数 itemClassName</li> 
   <li>渲染器增加参数 filterClassName</li> 
   <li>渲染器增加参数 cellClassName</li> 
  </ul> </li> 
 <li>select 
  <ul> 
   <li>增加参数 filterable</li> 
   <li>增加参数 filter-method</li> 
   <li>增加参数 remote</li> 
   <li>增加参数 remote-method</li> 
  </ul> </li> 
 <li>form 
  <ul> 
   <li>修复只读时内容溢出无法自动换行问题</li> 
   <li>修改表单校验显示错误提示问题</li> 
  </ul> </li> 
 <li>modal 
  <ul> 
   <li>修复拖动中断问题</li> 
   <li>修复设置 fullscreen 后第二次之后不自动全屏问题</li> 
  </ul> </li> 
 <li>toolbar 
  <ul> 
   <li>优化工具栏</li> 
  </ul> </li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/xuliangzhan_admin/vxe-table/releases/3.5.9">https://gitee.com/xuliangzhan_admin/vxe-table/releases/3.5.9</a></p>
                                        </div>
                                      
</div>
            