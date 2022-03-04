
---
title: 'Oracle Locking'
categories: 
 - 学习
 - Mind42
 - 分类
headimg: 'https://mind42.com/api/ajax/mindmapThumbnail?mindmapId=3b4182b0-ec76-4439-be0b-09d6e15f2e15&size=gallery'
author: Mind42
comments: false
date: 2022-03-04 05:08:54
thumbnail: 'https://mind42.com/api/ajax/mindmapThumbnail?mindmapId=3b4182b0-ec76-4439-be0b-09d6e15f2e15&size=gallery'
---

<div>   
<img src="https://mind42.com/api/ajax/mindmapThumbnail?mindmapId=3b4182b0-ec76-4439-be0b-09d6e15f2e15&size=gallery" referrerpolicy="no-referrer"><p>
                    An Oracle database has a lock table to control concurrent access to a database. When a user starts an update, it acquires a lock on the row, then does the update. If another user tries to update the same row, the second user will wait until the first user releases the lock. The problem is that if the first user never releases the lock, the second user will never be able to update the row.                </p>  
</div>
            