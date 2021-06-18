
---
title: 'Eclipse 4.20 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ad04f91245110630629aad9e052613d0353.png'
author: 开源中国
comments: false
date: Thu, 17 Jun 2021 23:43:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ad04f91245110630629aad9e052613d0353.png'
---

<div>   
<div class="content">
                                                                                            <p>Eclipse 4.20 正式发布，该版本更新内容包括：</p> 
<ul> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjdk.java.net%2F16%2F" target="_blank">Java 16</a>：Java 16 已经发布，Eclipse JDT 在 4.20 中支持 Java 16；</p> </li> 
 <li> <p>JUnit：org.eclipse.jdt.junit.runtime 和 org.eclipse.jdt.junit4.runtime 捆绑包需要的执行环境（BREE）现在是 JavaSE-1.8；</p> </li> 
 <li> <p>Java Editor：</p> 
  <ul> 
   <li> <p>快速修复「**创建新的局部变量」**已得到增强。当它创建一个变量作为 foreach 循环迭代的表达式时，它的类型是循环参数类型的数组：</p> <p>对于给定的代码：</p> <p><img alt="https://www.eclipse.org/eclipse/news/4.20/images/foreach-expression-type-before.png" src="https://oscimg.oschina.net/oscnet/up-ad04f91245110630629aad9e052613d0353.png" referrerpolicy="no-referrer"></p> <p>得到</p> <p><img alt="https://www.eclipse.org/eclipse/news/4.20/images/foreach-expression-type-after.png" src="https://oscimg.oschina.net/oscnet/up-8ce4d2258e43124b1fdcc552765f5a7d4f7.png" referrerpolicy="no-referrer"></p> </li> 
   <li> <p>使用 instanceof 清理：添加了一个新的清理，它使用 instanceof 表达式根据硬编码类检查对象。表达式必须是目标类的超类型。要应用清理，请在清理配置文件的代码样式选项卡上选中使用 instanceof 关键字而不是 Class.isInstance()复选框。</p> <p><img alt="https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a43f9667-87aa-4afb-90fb-01bbb9625b0c/Untitled.png" src="https://oscimg.oschina.net/oscnet/up-89d279c3c3bb37c67cbaf8b62626dc70158.png" referrerpolicy="no-referrer"></p> </li> 
   <li> <p>操作数分解清理：添加了一个新的清理，替换 (X && Y) || (X && Z) 为 (X && (Y || Y))。操作数必须是被动的和原始的。要应用清理，请选择清理配置文件中重复代码选项卡上的替换 (X && Y) || (X && Z) by (X && (Y || Z)) 的复选框。</p> <p><img alt="https://s3-us-west-2.amazonaws.com/secure.notion-static.com/01ac880a-c4d9-49ec-bdd2-9a7580a4b7a9/Untitled.png" src="https://oscimg.oschina.net/oscnet/up-2368a4a5c2b08cd83ec7253d826d4850eb3.png" referrerpolicy="no-referrer"></p> </li> 
   <li> <p>从 if/else 清理中取出重复的“if”：增加了一个新的清理方法，将重复的内部 if 条件移到外部 if 条件周围，内部 if 条件应该与外部 if 语句的两个 if/else 子句通用。要应用清理，请在清理配置文件中的重复代码标签上选择从 if/else 中提取重复的 "if "复选框；</p> <p><img alt="https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8f31c0af-2287-4fde-ba59-952f4b231355/Untitled.png" src="https://oscimg.oschina.net/oscnet/up-03f6088d1850f972e9118a3860236ea4a88.png" referrerpolicy="no-referrer"></p> </li> 
   <li> <p>Java 视图和对话框：区分正常导入和静态导入的搜索过滤器 该搜索视图现在支持专用于新的过滤器静态导入。此前的导入过滤器仅适用于非静态导入；</p> <p><img alt="https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a7f2d3a2-cb5e-4ccc-92f7-216191db628e/Untitled.png" src="https://oscimg.oschina.net/oscnet/up-35cededc31a2787bc08c4c1ae13d59122e8.png" referrerpolicy="no-referrer"></p> </li> 
   <li> <p>调试：复制运行配置项详细信息，新的复制按钮已添加到运行配置对话框的依赖项/类路径选项卡中，这可用于复制所选项目的详细信息；</p> <p><img alt="https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c2eec456-88d3-4b48-bdd7-6026a38b46d7/Untitled.png" src="https://oscimg.oschina.net/oscnet/up-ea456a8e9217b1095de02556046a2a527a6.png" referrerpolicy="no-referrer"></p> </li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.20%2Fjdt.php" target="_blank">https://www.eclipse.org/eclipse/news/4.20/jdt.php</a></p>
                                        </div>
                                      
</div>
            