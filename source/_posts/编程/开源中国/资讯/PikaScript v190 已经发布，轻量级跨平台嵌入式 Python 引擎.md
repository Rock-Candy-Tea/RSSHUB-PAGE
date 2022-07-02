
---
title: 'PikaScript v1.9.0 已经发布，轻量级跨平台嵌入式 Python 引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3614'
author: 开源中国
comments: false
date: Sat, 02 Jul 2022 01:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3614'
---

<div>   
<div class="content">
                                                                                            <p>PikaScript v1.9.0 已经发布，轻量级跨平台嵌入式 Python 引擎</p> 
<p>此版本更新内容包括：</p> 
<h2>概述</h2> 
<ol> 
 <li>可靠性大幅提高，在实际工程中受到检验并得到了大量的反馈。</li> 
 <li>包含大量实用的功能改进和错误修复。</li> 
</ol> 
<h2>功能更新</h2> 
<h3>内核</h3> 
<ol> 
 <li>支持 [] 字节的索引</li> 
 <li>支持 print() 和 str() 的 __str__ 魔法方法</li> 
 <li>支持 len() 和 __len()__ 魔法方法</li> 
 <li>支持 0o100 的八进制字面值</li> 
 <li>在 python 脚本中支持 Tab</li> 
 <li>为 pikaVM 检查栈溢出</li> 
 <li>支持 preCompiler 的 *.py 中 fuction 定义中的空行</li> 
 <li>支持 C 模块中的定义函数</li> 
 <li>支持 C 模块的 __del__() 魔法方法</li> 
 <li>支持类属性</li> 
 <li>支持使用 \ 合并多行代码</li> 
 <li>支持在其他 Python 文件中回调</li> 
 <li>支持 <None></li> 
 <li>支持虚拟中断和回调</li> 
 <li>支持获取 Kernal 版本</li> 
 <li>支持 d = &#123;'a':x, 'b':y, 'c': z&#125;.</li> 
 <li>支持 obj_runChar() 将char推送到 REPL</li> 
 <li>支持字符串和字节的切片</li> 
</ol> 
<h3>库</h3> 
<ol> 
 <li>支持 StdDevice 的读/写 Bytes API</li> 
 <li>添加 TemplateDevice 来测试 StdDevice 并提供参考演示</li> 
 <li>支持 chr()、hex()、ord()、id() 内置函数</li> 
 <li>支持 byte() 内置函数</li> 
 <li>支持 int() 转换 bytes，如 int(b'test'[0])</li> 
 <li>支持 int_to_bytes() 转换</li> 
 <li>支持 PikaStdDevice.Time() 的 unix 时间和 utc 时间</li> 
 <li>支持 printf() 的格式化输出和可变参数</li> 
 <li>支持 PikaStdDevice 的回调</li> 
</ol> 
<h2>错误修正</h2> 
<ol> 
 <li>ac5上的__user_free 错误</li> 
 <li>预编译器在最后需要两个空行</li> 
 <li>修复 cotex-M0 核心上的字节码对齐错误</li> 
 <li>修正遇到某些注释时的解析失败</li> 
 <li>修正遇到xx_import时的解析问题</li> 
 <li>1.'~-1'不等于'0'</li> 
 <li>a[1] = 1 在内部函数不工作</li> 
 <li>模块中的 for_loop runError</li> 
 <li>当字符串内部出现 '[' 时出现解析错误</li> 
 <li>当 str(PikaStdData.String('test')) 时出现内存泄漏</li> 
 <li>不能运行从其他模块导入的函数</li> 
 <li>用 arm-gcc 构建的 Bluepill 模板不适合 128K Flash</li> 
 <li>如果行尾是 <空格>，则Lexer有概率错误</li> 
 <li>创建 PikaStdDevice.Time() 时的异常输出</li> 
</ol> 
<h2>不兼容的更新</h2> 
<p>在 C 模块中使用 float 类型标注后，在 C 中的类型改为 double (之前是 float)</p> 
<h3>迁移指南</h3> 
<p>在 C 模块的 C 实现中使用 double</p> 
<p>详情查看：<a href="https://gitee.com/Lyon1998/pikascript/releases/v1.9.0">https://gitee.com/Lyon1998/pikascript/releases/v1.9.0</a></p>
                                        </div>
                                      
</div>
            