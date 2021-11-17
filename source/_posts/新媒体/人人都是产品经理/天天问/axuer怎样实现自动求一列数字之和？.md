
---
title: 'axuer怎样实现自动求一列数字之和？'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 天天问
headimg: 'https://static.woshipm.com/YY_C_20211117_1637119336232083655.jpg'
author: 人人都是产品经理
comments: false
date: Wed, 17 Nov 2021 07:08:54 GMT
thumbnail: 'https://static.woshipm.com/YY_C_20211117_1637119336232083655.jpg'
---

<div>   
<p>我们在做一些高保真原型时常常会用中继器实现动态的表格展示效果，用来演示增删改查的交互是非常不错的，但是表格经常会有统计某一列数字之和的需求，那么怎样才能实现自动汇总中继器某一列数字之和呢？<br></p><p><img src="https://static.woshipm.com/YY_C_20211117_1637119336232083655.jpg" title="TTW_QUESTION_202111_20211117110307_0845.jpg" alt="1637114086(1).jpg" referrerpolicy="no-referrer"><img src="https://static.woshipm.com/YY_C_20211117_1637119336541091162.jpg" title="TTW_QUESTION_202111_20211117110317_0743.jpg" alt="1637114036(1).jpg" referrerpolicy="no-referrer"></p><p>中继器现有的求和函数只是   value1 + value2   这样的，用运算符将两个值相加的形式，那么这样只能想办法获取不同行的数值。</p><p>但中继器本身就好似一个“重复器”，拖进去的元件会产生生出这个元件的许多“分身”，虽然它的分身有不同的“面貌”，但是它的“本体”却永远只有一个，中继器的函数只是对“本体”进行编辑，我们无法准确的获取到一个元件“分身1、分身2、分身3.....分身N”，所以不能对所有“分身”上的数值进行汇总。</p><p>那么有没有其他思路能够实现上面的数据汇总效果呢？真希望Axuer更新这样的统计函数</p>  
</div>
            