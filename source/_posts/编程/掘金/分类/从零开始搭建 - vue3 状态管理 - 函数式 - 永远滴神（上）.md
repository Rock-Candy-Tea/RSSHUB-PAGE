
---
title: '从零开始搭建 - vue3 状态管理 - 函数式 - 永远滴神（上）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad43ddb6b80f4279b03ef866e1fd91da~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 04 Jun 2021 04:29:48 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad43ddb6b80f4279b03ef866e1fd91da~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:18px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:40px;margin-bottom:20px;color:#007fff;display:flex;align-items:center&#125;.markdown-body h1:hover:before,.markdown-body h2:hover:before,.markdown-body h3:hover:before,.markdown-body h4:hover:before,.markdown-body h5:hover:before,.markdown-body h6:hover:before&#123;transition:All .4s ease-in-out;transform:rotate(1turn)&#125;.markdown-body h1&#123;font-size:30px;background:linear-gradient(#fff 60%,#c6e3ff 0)&#125;.markdown-body h1:before&#123;content:"";display:inline-block;width:32px;height:32px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h2&#123;font-size:24px;background:linear-gradient(#fff 60%,#cce3fb 0)&#125;.markdown-body h2:before&#123;content:"";display:inline-block;width:24px;height:24px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h3&#123;font-size:20px&#125;.markdown-body h3:before&#123;content:"";display:inline-block;width:18px;height:18px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h4&#123;font-size:18px&#125;.markdown-body h4:before&#123;content:"";display:inline-block;width:16px;height:16px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h5&#123;font-size:16px&#125;.markdown-body h5:before&#123;content:"";display:inline-block;width:15px;height:15px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h6&#123;font-size:14px&#125;.markdown-body h6:before&#123;content:"";display:inline-block;width:12px;height:12px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;border-bottom:2px solid #007fff;color:#007fff;padding-right:10px&#125;.markdown-body p&#123;letter-spacing:1px;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;display:block;max-width:100%;margin:10px auto&#125;.markdown-body hr&#123;border:none;border-top:1px dashed #92c8ff&#125;.markdown-body hr:before&#123;content:"✂";display:inline-block;position:relative;top:-12px;left:40px;padding:0 3px;color:#007fff;font-size:18px&#125;.markdown-body hr:after&#123;content:"按虚线剪开";position:relative;top:-15px;left:84%;padding:0 3px;color:#007fff;font-size:12px&#125;.markdown-body del&#123;color:#f44&#125;.markdown-body em&#123;color:#007fff;margin:0 2px&#125;.markdown-body strong&#123;color:#007fff;font-weight:bolder&#125;.markdown-body code&#123;word-break:break-word;border-radius:4px;overflow-x:auto;background-color:#e6f3ff;color:#007fff;font-weight:600;font-size:16px;padding:.065em .4em;border:1px solid #007fff&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:5px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:18px;font-weight:400;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8;border:none&#125;.markdown-body a&#123;text-decoration:none;color:#007fff;border-bottom:1px solid #007fff&#125;.markdown-body a:before&#123;content:"¶";margin-right:5px;font-size:22px&#125;.markdown-body a:after&#123;content:"↷";margin-left:2px;font-size:22px;display:none&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c;border-bottom:1px solid #275b8c&#125;.markdown-body a:active:after,.markdown-body a:hover:after&#123;display:inline-block&#125;.markdown-body table&#123;display:inline-block!important;font-size:16px;width:auto;max-width:100%;overflow:auto;border:1px solid #a5d3ff&#125;.markdown-body thead&#123;background:#c6e3ff;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#eef7ff&#125;.markdown-body tbody>tr:nth-child(odd)&#123;background-color:#f8fcff&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #007fff;background-color:#eef7ff&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol li::marker,.markdown-body ul li::marker&#123;color:#007fff&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">主题</h1>
<p>从零撸一个<code>vue3状态管理</code></p>
<blockquote>
<p>不是vuex，不是vuex，不是vuex，重要的事情说三遍。</p>
</blockquote>
<h1 data-id="heading-1">原因</h1>
<p>为啥有了官方生态的<code>vuex</code>，还要自己动手撸一个类似的状态管理呢？</p>
<ol>
<li><code>vuex</code>的api比较反直觉。（不过据说5.x版本起会好一些）</li>
<li>刚好最近在深入<code>js函数式</code>，所以想写一个偏函数式的状态管理库。</li>
</ol>
<h1 data-id="heading-2">学习前提</h1>
<h2 data-id="heading-3">技术栈</h2>
<ol>
<li>vue3</li>
<li>vite</li>
<li>tailwind css</li>
</ol>
<blockquote>
<p>技术栈中的<code>2,3</code>可以不用理，因为不是很重要。</p>
</blockquote>
<h2 data-id="heading-4">前置知识</h2>
<ol>
<li>JavaScript</li>
<li>vue3</li>
</ol>
<blockquote>
<p>特别是<code>JavaScript</code>的基础。对闭包，proxy，函数相关知识点要求比较高。</p>
</blockquote>
<h1 data-id="heading-5">丢弃</h1>
<blockquote>
<p>先来看看<code>vuex</code>官方的架构图</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad43ddb6b80f4279b03ef866e1fd91da~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
从上图可以看到 <code>mutation</code> 行为更多的作为一个与 <code>devtool</code> 沟通的角色。但是其实很多前端人的项目并没复杂到那种程度，以至于大家与<code>devtool</code>形同陌路人。在这里为了降低复杂度，所以把它删掉了，当然要实现也不算难。</p>
<blockquote>
<p>来看看<code>vuex</code>的思想架构图</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8e15c94bf8a4f0d9f8e33c16393ac5b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上图可以发现，其实<code>view</code>并不能算是<code>vuex</code>状态管理的一部分。
所以我们可以得出关于状态管理的思想架构图。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37974612260842b78717a4903660c620~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
即<code>state</code>(状态)与<code>action</code>(变动)。（本节会围绕其来进行讲解）</p>
<h1 data-id="heading-6">状态</h1>
<p>我们都知道在<code>vue3</code>中有两个主要的响应式api，<code>ref</code>和<code>reactive</code>。我们这里使用<code>reactive</code>。先来回顾一下它的基本使用。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">main</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"add"</span>></span>&#123;&#123;v.num&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">main</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123; reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
    
    <span class="hljs-keyword">const</span> v = reactive(&#123; <span class="hljs-attr">num</span>: <span class="hljs-number">0</span> &#125;)
    
    <span class="hljs-keyword">const</span> add = <span class="hljs-function">() =></span> v.num++
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>于是鼠标点击<code>main元素</code>的时候，就会执行<code>加操作</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/060d1d5e11b242e1b019e42745c2ad32~tplv-k3u1fbpfcp-watermark.image" alt="1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以即使这样，状态<code>v</code>也无法被其他组件共享。
例如你<code>foo组件</code>和<code>bar组件</code>。他们都维护着状态<code>v</code>。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03bbe5636a8a4d328dad3b6f4ec3c8ed~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时去更新其中一个组件的状态<code>v</code>时，另一个组件的状态<code>v</code>是不会被更新。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dea689b1a1204a7ab9b24e5fa68d582d~tplv-k3u1fbpfcp-watermark.image" alt="2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>于是我们想到可以将状态<code>v</code>抽离出来作为一个共享的状态。此时再去修改该状态<code>v</code>就会反应到每个依赖它的组件上。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4720e87551864a21868f15f247ed4f1b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>反映到代码上就是用一个<code>js模块</code>去抽离状态<code>v</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// use/store.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> v = reactive(&#123; <span class="hljs-attr">num</span>: <span class="hljs-number">1</span> &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后让组件们去依赖它（引入）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// components/foo.vue && components/bar.vue</span>
<template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">main</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"add"</span>></span>&#123;&#123;v.num&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">main</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123; v &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../use/store"</span>
    
    <span class="hljs-keyword">const</span> add = <span class="hljs-function">() =></span> v.num++
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时再去点击<code>foo</code>组件或者<code>bar</code>组件，状态都会统一地更新。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afff97c5f7ee4b9197e0f3b7f0e2cf50~tplv-k3u1fbpfcp-watermark.image" alt="3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是现在还有一个问题，就是状态<code>v</code>的变动管理是混乱的。例如<code>foo</code>组件和<code>bar</code>组件都能对状态的变动进行自定义。两者都定义了<code>add</code>加操作变动。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/726981f4e33a4af6af9013421ee5897f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// components/foo.vue</span>
<template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">main</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"add"</span>></span>foo - &#123;&#123;v.num&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">main</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123; v &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../use/store"</span>
    
    <span class="hljs-comment">// 定义了状态的变动</span>
    <span class="hljs-keyword">const</span> add = <span class="hljs-function">() =></span> v.num++
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="hljs-comment">// components/bar.vue</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">main</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"add"</span>></span>bar - &#123;&#123;v.num&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">main</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123; v &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../use/store"</span>
    
    <span class="hljs-comment">// 定义了状态的变动</span>
    <span class="hljs-comment">// 原本需要的是加操作，却被写成了减操作</span>
    <span class="hljs-keyword">const</span> add = <span class="hljs-function">() =></span> v.num--
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时再去点击，就会发现跟原先预想的不一样。点击<code>bar</code>组件变成了<code>减操作</code>。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d21367283ee54d90a41d4503eb344211~tplv-k3u1fbpfcp-watermark.image" alt="4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可能你会觉得谁会犯这种低级错误呢。但是如果有超级多的组件共享该状态，那么的状态的变动将不可预测，同时也会催生bug，排查也会更难。</p>
<h1 data-id="heading-7">变动</h1>
<p>还是老样子，将变动的定义抽出来统一管理就可以了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9666f6cef66a4d2793abd1539e7151f1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// use/store.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> v = reactive(&#123; <span class="hljs-attr">num</span>: <span class="hljs-number">1</span> &#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> add = <span class="hljs-function">() =></span> v.num++
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时变成在一个<code>模块</code>里维护状态变动，可维护性直线上升。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// components/foo.vue</span>
<template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">main</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"add"</span>></span>foo - &#123;&#123;v.num&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">main</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123; v, add &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../use/store"</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="hljs-comment">// components/bar.vue</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">main</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"add"</span>></span>bar - &#123;&#123;v.num&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">main</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123; v, add &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../use/store"</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">整合</h1>
<p>之前都在讲状态共享的基础原理，接下来要做一个<code>api</code>的整合。整合的目的是更好的状态管理。</p>
<blockquote>
<p>以下是我自己的封装风格，偏函数式了一点</p>
</blockquote>
<h2 data-id="heading-9">响应式状态</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 整合api</span>
<span class="hljs-comment">// use/store.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> useStore = <span class="hljs-function"><span class="hljs-params">v</span> =></span> &#123;

    <span class="hljs-comment">// 设置`状态`为响应式</span>
    v = reactive(v)
    
    <span class="hljs-comment">// 暴露响应式的`状态`</span>
    <span class="hljs-keyword">return</span> &#123; v &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; useStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../use/store.js"</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> &#123; v &#125; = useStore(&#123; <span class="hljs-attr">num</span>: <span class="hljs-number">0</span> &#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> add = <span class="hljs-function">() =></span> v.num++
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">变动的定义</h2>
<blockquote>
<p>由于<code>变动</code>是函数，函数又相对比较灵活，所以我做了以下<code>变动定义</code>的封装。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 整合api</span>
<span class="hljs-comment">// use/store.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> useStore = <span class="hljs-function"><span class="hljs-params">v</span> =></span> &#123;

    <span class="hljs-comment">// 设置`状态`为响应式</span>
    v = reactive(v)
    
    <span class="hljs-comment">// 定义 `变动定义` 为 高阶函数，这里后边会讲</span>
    <span class="hljs-keyword">const</span> act = <span class="hljs-function"><span class="hljs-params">fn</span> =></span> <span class="hljs-function"><span class="hljs-params">nv</span> =></span> fn(v, nv)
    
    <span class="hljs-comment">// 暴露响应式的`状态`</span>
    <span class="hljs-keyword">return</span> &#123; v &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; useStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../use/store.js"</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> &#123; v, act &#125; = useStore(&#123; <span class="hljs-attr">num</span>: <span class="hljs-number">0</span> &#125;)

<span class="hljs-comment">// const add = () => v.num++</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> add = act(<span class="hljs-function"><span class="hljs-params">v</span> =></span> v.num++)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">act</h3>
<p>上边的封装比较难的就是<code>act</code>这个<code>变动定义</code>。</p>
<ol>
<li>命名: <code>act</code>是<code>action</code>的缩写，之所以选择这个命名，大概因为我是个简洁怪吧。</li>
<li><code>fn => nv => fn(v, nv)</code> <code>fn</code>是变动回调，<code>v</code>是响应式状态源,<code>nv</code>是新的状态源（在<code>vuex</code>中被称为<code>payload</code>载荷）</li>
<li>假如第二点看不懂的话，先用起来用得多了自然就懂了。</li>
</ol>
<blockquote>
<p>好像就只有这一个地方用了比较函数式的点😂</p>
</blockquote>
<h3 data-id="heading-12">用法示例</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; useStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../use/store.js"</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> &#123; v, act &#125; = useStore(&#123; <span class="hljs-attr">num</span>: <span class="hljs-number">0</span> &#125;)

<span class="hljs-keyword">const</span> add = act(<span class="hljs-function"><span class="hljs-params">v</span> =></span> v.num++)

<span class="hljs-keyword">const</span> subtract = act(<span class="hljs-function"><span class="hljs-params">v</span> =></span> v.num--)

<span class="hljs-keyword">const</span> set = act(<span class="hljs-function">(<span class="hljs-params">v, nv</span>) =></span> v.num = nv)

add() <span class="hljs-comment">// v.num将加1，此时v.num为1</span>
add() <span class="hljs-comment">// v.num将加1，此时v.num为2</span>

subtract() <span class="hljs-comment">// v.num将减1，此时v.num为1</span>

set(<span class="hljs-number">1</span>) <span class="hljs-comment">// v.num将被设置为1，这里得第一实参就是上边的 nv</span>
set(<span class="hljs-number">100</span>) <span class="hljs-comment">// v.num将被设置为100</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-13">尾声</h1>
<p>不知不觉写了1000多个字，也做了非常多的图去帮助大家理解，相信能给大家在<code>状态管理</code>上带来帮助。后续的文章会给大家带来<code>dep</code>，<code>sub</code>等更体系化的<code>状态管理</code>实现。</p></div>  
</div>
            