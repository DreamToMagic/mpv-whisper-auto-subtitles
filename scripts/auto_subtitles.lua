local mp = require 'mp'
local utils = require 'mp.utils'

mp.register_event("file-loaded", function()
    local path = mp.get_property("path")
    local abs_path = mp.command_native({"expand-path", path})

    local args = {
        "python", "whisper_sub.py", abs_path
    }
    mp.osd_message("⏳ 正在生成字幕，请稍候...")
    utils.subprocess_detached({ args = args })
end)
