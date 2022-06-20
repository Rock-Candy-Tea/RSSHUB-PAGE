
---
title: 'SurveyKing v0.3.0 正式发布：最强开源考试和调查问卷系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b00c0362f7827c7927569d4ce5dc6792d93.png'
author: 开源中国
comments: false
date: Mon, 20 Jun 2022 09:26:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b00c0362f7827c7927569d4ce5dc6792d93.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>SurveyKing（卷王）v0.3.0 版本经过4个月的不断迭代，终于发布正式版本了。卷王是已知安装最简单、功能最强大的开源调查问卷系统，支持<strong>考试</strong>、<strong>调查问卷</strong>、<strong>公开查询</strong>、<strong>投票</strong>等。</p> 
<p>功能概览：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>安装简单，</strong>安装包只有40M,支持一键启动</li> 
 <li><strong>题型丰富</strong>，支持 20 多种常用题型</li> 
 <li><strong>多种创建问卷的方式</strong>，支持 <strong>Excel导入问卷</strong>、<strong>文本导入创建问卷(支持填空、单选、下拉、级联、横向填空等题的文本导入)</strong>、<strong>问卷编辑器拖拽创建</strong></li> 
 <li><strong>富文本</strong>，所有问题和选项标题都支持富文本，支持插入视频、音频、图片、数学公式等</li> 
 <li><strong>白名单答题</strong>，支持系统内用户白名单和外部导入用户白名单</li> 
 <li><strong>公开查询</strong>，支持对答案进行公开查询，支持自定义查询条件，自定义要显示的查询结果，支持查询签名、查询字段权限控制（隐藏字段、字段只读、字段可编辑）</li> 
 <li><strong>自定义校验</strong>，可以<strong>设置填空题的类型(</strong>如邮箱、身份证、数字、汉字、日期、时间等)，可以<strong>设置数值、日期的范围</strong>。同时支持更高级的校验设置，根据多个问题的答案<strong>联动设置校验</strong>，并支持设置<strong>自定义校验消息</strong></li> 
 <li><strong>支持多种逻辑计算设置</strong> 
  <ul style="margin-left:0; margin-right:0"> 
   <li>显示逻辑，根据选项结果来控制问题的显示隐藏</li> 
   <li>计算逻辑，如根据身高体重自动计算BMI、根据身份证号自动计算年龄和性别</li> 
   <li>校验逻辑，支持对答案进行校验，并可以自定义错误提示信息</li> 
   <li>文本替换逻辑，根据不同的答案显示不同的提示语</li> 
  </ul> </li> 
 <li><strong>多种设置</strong>，如设置问题默认答案、显示答题次数、显示答题卡、<strong>问卷白名单设置</strong>等等</li> 
 <li><strong>页面美观，响应式布局</strong>，自动适配 PC 端和手机端</li> 
 <li><strong>数据展示</strong>，提供 excel 般的在线数据编辑体验</li> 
 <li><strong>数据导出</strong>，支持导出Excel、打包导出附件，独创的附件名导出变量(如可以根据问题答案动态的对附件进行重命名)</li> 
 <li><strong>数据报表</strong>，支持对单选、多选、级联、数字填空、下拉等题型实时统计分析，并以图表（条形图、柱状图、<span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zhihu.com%2Fsearch%3Fq%3D%25E6%2589%2587%25E5%25BD%25A2%25E5%259B%25BE%26search_source%3DEntity%26hybrid_search_source%3DEntity%26hybrid_search_extra%3D%257B%2522sourceType%2522%253A%2522answer%2522%252C%2522sourceId%2522%253A2527508777%257D" target="_blank">扇形图</a></span>）和数据表格对答案实时分析</li> 
</ul> 
<h2>调查问卷系统</h2> 
<p>所有问题和选项都支持富文本，并且支持多种设置</p> 
<p><img height="1758" src="https://oscimg.oschina.net/oscnet/up-b00c0362f7827c7927569d4ce5dc6792d93.png" width="2586" referrerpolicy="no-referrer"></p> 
<p> </p> 
<h2>考试系统</h2> 
<p>支持多种计分方式，支持刷题模式，支持考试完成公开查询考试分数等等。</p> 
<p><img height="1854" src="https://oscimg.oschina.net/oscnet/up-3fe2568736f52581e625dd3f1928a25fef0.png" width="2658" referrerpolicy="no-referrer"></p> 
<h2>公开查询系统</h2> 
<p>支持比金山快查和易查分更丰富的查询设置。</p> 
<p> </p> 
<p><img height="1676" src="https://oscimg.oschina.net/oscnet/up-612f3f2ed189049e188c06828dfd0e937cb.png" width="1620" referrerpolicy="no-referrer"></p> 
<h2> </h2> 
<h2>更多功能介绍</h2> 
<h3>多种问卷设置</h3> 
<p>提供了很多问卷设置，所有的设置允许自由组合。</p> 
<p><img height="1562" src="https://oscimg.oschina.net/oscnet/up-4aea56e1602cbf3684825a893b8ca200314.png" width="2656" referrerpolicy="no-referrer"></p> 
<h3>数据表格</h3> 
<p>基于 canvas-grid 魔改的数据表格，提供 Excel 般的数据操作体验。</p> 
<p>提供了导入数据和导出数据</p> 
<p><img height="1562" src="https://oscimg.oschina.net/oscnet/up-f03cf647bc04b6e000be64ead1551f4bba9.png" width="2678" referrerpolicy="no-referrer"></p> 
<p>卷王的导出数据功能也领先问卷网、问卷星和腾讯问卷等，多种导出方式自由组合。独创的导出附件命名变量，允许你自定义导出的附件名称。</p> 
<p><img height="1096" src="https://oscimg.oschina.net/oscnet/up-dedfb5a1bf32aa3fd79e28932cff35be88b.png" width="1538" referrerpolicy="no-referrer"></p> 
<h3>多种问题导入方式</h3> 
<p>支持文本导入题库，支持 Excel 模板导入题库</p> 
<p><img height="1542" src="https://oscimg.oschina.net/oscnet/up-caafd6bb7e785816d9835252635dce76adb.png" width="2638" referrerpolicy="no-referrer"></p> 
<h3>数据报表</h3> 
<p>对单选、多选、下拉、级联、数值填空等题支持实时的报表统计分析，并以多种图表和表格方式展示</p> 
<p><img height="1872" src="https://oscimg.oschina.net/oscnet/up-fd0706f472066f6b5ad7159c2342978acc0.png" width="2372" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            