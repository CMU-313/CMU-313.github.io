-- learning-goals.lua
-- Pandoc Lua filter that populates any Div with class `learning-goals-list`
-- using the `learning_goals` sequence from the document's YAML front matter.
--
-- Usage in any slide:
--
--   ## Learning Goals { .learning-goals-slide }
--
--   ::: {.learning-goals-list}
--   :::
--
-- The same placeholder also works on the summary slide so goals only need to
-- be written once (in the YAML front matter).
--
-- Registered project-wide via `filters:` in _metadata.yml.

-- Two-pass filter: first capture Meta, then expand the placeholder Divs.
return {
  -- Pass 1: read the learning goals out of the document metadata.
  {
    Meta = function(meta)
      _learning_goals_meta = meta['learning_goals']
      return meta
    end
  },
  -- Pass 2: replace every Div that carries the `learning-goals-list` class.
  {
    Div = function(div)
      if not div.classes:includes('learning-goals-list') then
        return nil  -- leave the block unchanged
      end
      if not _learning_goals_meta then
        return {}   -- no goals defined — emit nothing
      end

      local items = {}
      for _, goal in ipairs(_learning_goals_meta) do
        -- Each entry is MetaInlines; preserve any inline formatting.
        table.insert(items, { pandoc.Plain(pandoc.Inlines(goal)) })
      end
      return { pandoc.BulletList(items) }
    end
  }
}
